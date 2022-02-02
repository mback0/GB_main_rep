def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    values = []
    indices = []
    for val in list_in:
        val_to_list = list(val)
        if val.isdigit() == True:
            indices.append(list_in.index(val))
            if int(val) < 10:
                j = '0{}'.format(val)
                values.append(j)
            else:
                values.append(val)
        else:
            for z in val_to_list:
                if z.isdigit() == True:
                    indices.append(list_in.index(val))
                    x = val[1:]
                    if int(x) < 10:
                        h = '{}0{}'.format(val[:1], x)
                        values.append(h)
                        break
                    else:
                        values.append(val)
                        break
    count_1 = 0
    while count_1 < len(values):
        list_in[indices[count_1]] = values[count_1]
        count_1 += 1

    count_2 = 0
    for i in indices:
        list_in.insert(count_2 + i, "''")
        count_2 += 1
        list_in.insert(count_2 + i + 1, "''")
        count_2 += 1

    str_out = ' '.join(list_in)
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

