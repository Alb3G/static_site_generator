import os	
from gen_page import gen_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            # Solo procesar archivos .md
            name, ext = os.path.splitext(from_path)
            if ext.lower() == ".md":
                dest_html_path = os.path.splitext(dest_path)[0] + ".html"
                gen_page(from_path, template_path, dest_html_path, base_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, base_path)
