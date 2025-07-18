import os
import shutil
import sys
from gen_page import gen_page
from generate_pages_recursive import generate_pages_recursive

def copy_files_recursive(source_dir_path, dest_dir_path):
	if not os.path.exists(dest_dir_path):
		os.mkdir(dest_dir_path)

	for filename in os.listdir(source_dir_path):
		from_path = os.path.join(source_dir_path, filename)
		dest_path = os.path.join(dest_dir_path, filename)
		print(f" * {from_path} -> {dest_path}")
		if os.path.isfile(from_path):
			shutil.copy(from_path, dest_path)
		else:
			copy_files_recursive(from_path, dest_path)

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"	
default_basepath = "/"

def main():
	base_path = default_basepath
	if len(sys.argv) > 1:
		basepath = sys.argv[1]

	print("Deleting public directory...")
	if os.path.exists(dir_path_docs):
		shutil.rmtree(dir_path_docs)

	print("Copying static files to public directory...")
	copy_files_recursive(dir_path_static, dir_path_docs)

	print("Generating content...")
	generate_pages_recursive(base_path, template_path, dir_path_docs, base_path)
	

if __name__ == "__main__":
	main()