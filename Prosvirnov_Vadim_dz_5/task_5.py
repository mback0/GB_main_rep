def get_uniq_numbers(src: list):
    un_numb = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            un_numb.add(el)
        else:
            un_numb.discard(el)
        tmp.add(el)
    result = [x for x in src if x in un_numb]
    return result

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))