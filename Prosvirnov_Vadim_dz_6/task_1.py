from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    ip_idx = line.index('-')
    ip = line[:ip_idx - 1]
    method_idx_start = line.find('"') + 1
    method_idx_end = line.find('/', method_idx_start + 1) - 1
    dir_idx = line.find('HTTP')
    method = line[method_idx_start:method_idx_end]
    dir = line[method_idx_end + 2 - 1:dir_idx - 1]
    return ip, method, dir


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for l1 in fr:
        list_out.append(get_parse_attrs(l1))


pprint(list_out)