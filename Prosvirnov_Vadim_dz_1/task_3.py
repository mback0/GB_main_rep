def transform_string(number: int) -> str:
    phrase = ""
    to_str = str(number)
    to_int = int(to_str[-1])
    if number >= 11 and 19 >= number:
        phrase = "процентов"

    elif to_str[-1] == '1':
        phrase = "процент"

    elif to_int >=2 and 4 >= to_int:
        phrase = "процента"

    elif to_int >=5 and 9 >= to_int :
        phrase = "процентов"
    else:
        phrase = "процентов"
    result = "{} {}".format(number, phrase)
    return result


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))