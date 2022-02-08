to_ru_dict = {'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    if value.istitle() == True:
        str_out = to_ru_dict.get(value.lower()).title()
    else:
        str_out = to_ru_dict.get(value)
    return str_out
print(num_translate_adv('Two'))
