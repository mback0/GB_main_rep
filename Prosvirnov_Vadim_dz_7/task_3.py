import os.path
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(BASE_DIR, 'my_project')

for path, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.html'):
            templates_path = os.path.join(project_dir, 'templates')
            os.makedirs(templates_path, exist_ok=True)
            dir_path_and_name = os.path.split(path)
            dir_in_templates_path = os.path.join(templates_path, dir_path_and_name[1])
            os.makedirs(dir_in_templates_path, exist_ok=True)
            copy_file_path = os.path.join(dir_in_templates_path, file)
            if not os.path.exists(copy_file_path):
                orig_file_path = os.path.join(path, file)
                shutil.copy2(orig_file_path, dir_in_templates_path)
