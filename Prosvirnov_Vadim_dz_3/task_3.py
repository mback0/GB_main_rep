def thesaurus(*args) -> dict:
    list_1 = list(map(list, args))
    dict_out = {}
    for i in list_1:
        dict_out.setdefault(i[0], 'none')
    for k, v in dict_out.items():
        list_2 = []
        for z in args:
            if z[0] == k and z not in list_2:
                list_2.append(z)
        dict_out[k] = list_2

    return dict_out

print(thesaurus("Макар", "Иван", "Мария", "Петр", "Илья", "Константин", "Евгений", "Корней", "Евгений"))