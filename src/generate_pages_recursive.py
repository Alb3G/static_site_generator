import os	
from gen_page import gen_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            name, _ = os.path.splitext(dest_path)
            dest_path = name + ".html"
            gen_page(from_path, template_path, dest_path, base_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, base_path)
