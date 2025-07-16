import os
import shutil
from utils.markdown_to_htmlnode.markdown_to_html_node import markdown_to_html_node
from utils.extract_markdown_title.extract_markdown_title import extract_title

def gen_page(from_path: str, template_path: str, dest_path: str):
	from_path_file_name = os.path.dirname(from_path)
	dest_path_file_name = os.path.dirname(dest_path)
	template_path_file_name = os.path.dirname(template_path)
	print(f"Generating page from {from_path_file_name} to {dest_path_file_name}, using {template_path_file_name}")
	# read md and template files
	with open(from_path, "r", encoding="utf-8") as file:
		md_file_content = file.read()
	with open(template_path, "r", encoding="utf-8") as file:
		template = file.read()
	# transform text to html content
	html_from_from_md = markdown_to_html_node(md_file_content).to_html()
	md_title = extract_title(md_file_content).replace("#", "").strip()
	# replace template tags for new generated content
	template = template.replace("{{ Title }}", md_title).replace("{{ Content }}", html_from_from_md)
	# write the new template
	dest_path_dirs = os.path.dirname(dest_path)
	os.makedirs(dest_path_dirs, exist_ok=True)
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
	template_path = "/Users/albertoguzman/Code/static_site_generator/template.html"
	main_content_path = "/Users/albertoguzman/Code/static_site_generator/content/content.md"
	glorfindel_content_path = "/Users/albertoguzman/Code/static_site_generator/content/blog/glorfindel/index.md"
	template_dest_path = f"{dest}/index.html"
	glorfindel_template_dest_path = f"{dest}/blog/glorfindel.html"
	gen_build(src, dest)
	gen_page(main_content_path, template_path, template_dest_path)
	gen_page(glorfindel_content_path, template_path, glorfindel_template_dest_path)

if __name__ == "__main__":
	main()