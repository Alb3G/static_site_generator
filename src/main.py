import os
import shutil
from utils.markdown_to_htmlnode.markdown_to_html_node import markdown_to_html_node
from utils.extract_markdown_title.extract_markdown_title import extract_title

def gen_page(from_path: str, template_path: str, dest_path: str):
	print(f"Generating page from {from_path} to {dest_path}, using {template_path}")
	# read md and template files
	md_file_content = ""
	template = ""
	with open(from_path, "r", encoding="utf-8") as file:
		md_file_content = file.read()
	with open(template_path, "r", encoding="utf-8") as file:
		template = file.read()
	# transform text to html content
	html_from_from_md = markdown_to_html_node(md_file_content).to_html()
	md_title = extract_title(md_file_content)
	# replace template tags for new generated content
	template.replace("{{ Title }}", md_title)
	template.replace("{{ Content }}", html_from_from_md)
	# write the new template
	with open(dest_path, "w", encoding="utf-8") as file:
		file.write(template)
	

def gen_build(src: str, dest: str):
	shutil.rmtree(dest, ignore_errors=True)
	os.makedirs(dest, exist_ok=True)
	
	for item in os.listdir(src):
		item_in_src = f"{src}/{item}"
		if os.path.isfile(item_in_src):
			shutil.copy2(item_in_src, dest)
		else:
			dest_dir = f"{dest}/{item}"
			os.mkdir(dest_dir)
			gen_build(item_in_src, dest_dir)
	
	return

def main():
	src = "/Users/albertoguzman/Code/static_site_generator/static"
	dest = "/Users/albertoguzman/Code/static_site_generator/public"
	gen_build(src, dest)

if __name__ == "__main__":
	main()