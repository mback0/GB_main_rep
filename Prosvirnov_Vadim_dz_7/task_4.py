import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(BASE_DIR, 'some_data')

files_path = []
for path, dirs, files in os.walk(data_dir_path):
    [files_path.append(os.path.join(str(path), str(file))) for file in files]
t_dict = {100: 0, 1000: 0, 10000: 0, 100000: 0}
out_of = 0
for file in files_path:
    if os.stat(file).st_size < 100:
        t_dict[100] += 1
    elif os.stat(file).st_size > 100 and os.stat(file).st_size < 1000:
        t_dict[1000] += 1
    elif os.stat(file).st_size > 1000 and os.stat(file).st_size < 10000:
        t_dict[10000] += 1
    elif os.stat(file).st_size > 10000 and os.stat(file).st_size < 100000:
        t_dict[100000] += 1
    else:
        out_of += 1

print(t_dict)
print(f'Значений, вышедших за пределы начального словаря (размер больше 100000) : {out_of}')
