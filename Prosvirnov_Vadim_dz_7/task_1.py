import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_name = 'my_project_task_1'
project_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

main_project_dir = os.path.join(BASE_DIR, project_name)
os.makedirs(main_project_dir, exist_ok=True)
[os.makedirs(os.path.join(main_project_dir, dir), exist_ok=True) for dir in project_dirs]

"""
Переименовал название проекта, чтобы при тестах не было конфликтов с заданием 3, т.к не успеваю сделать задание 2
"""