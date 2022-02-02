def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_len = len(list_in)
    list2 = []
    for x in list_in:
        y = x.split(' ')
        list2.append(y[-1].title())
    list_out = []

    idx = 0
    while idx < list_len:
        list_out.append('Привет, {}!'.format(list2[idx]))
        idx += 1
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита',]
result = convert_name_extract(my_list)
print(result)