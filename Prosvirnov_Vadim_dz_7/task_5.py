import os.path
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(BASE_DIR, 'some_data')

files_path = []
for path, dirs, files in os.walk(data_dir_path):
    [files_path.append(os.path.join(str(path), str(file))) for file in files]
f_dict = {}

def t_func(min, max):
    f_dict.setdefault(max)
    count = 0
    ext = []
    for file in files_path:
        if os.stat(file).st_size < max and os.stat(file).st_size > min:
            count += 1
            x = os.path.split(file)[1]
            y = x.split('.')[1]
            if y not in ext:
                ext.append(y)
    f_dict[max] = tuple([count, ext])


t_func(0,100)
t_func(100,1000)
t_func(1000,10000)
t_func(10000,100000)
print(f_dict)

with open('_summary.json', 'w', encoding='utf-8') as fw:
    json.dump(f_dict, fw, indent=2)