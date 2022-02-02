from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    roubles = []
    cents = []
    for x in list_in:
        list_1 = []
        z = str(x)
        list_1.append(z.split('.'))
        list_2 = list_1[0]
        roubles.append(list_2[0])
        cents.append(list_2[1])

    count_1 = 0
    while count_1 < len(cents):
        if int(cents[count_1]) < 10 and len(cents[count_1]) < 2:
            cents[count_1] = '0{}'.format(cents[count_1])
        count_1 += 1


    count_2 = 0
    while count_2 < len(list_in):
        list_in[count_2] = '{} руб {} коп'.format(roubles[count_2], cents[count_2])
        count_2 += 1
    str_out = ", ".join(list_in)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(f'a) Итоговая строка: {result_1}')


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in

print('b) id исходного списка: {}'.format(id(my_list)))
print('Исходный список: {}'.format(my_list))
result_2 = sort_prices(my_list)
print('Отсортированный по возврастанию список: {}'.format(my_list))
print('id списка после сортировки: {}'.format(id(result_2)))



def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_in.sort()
    list_out = list(reversed(list_in))
    return list_out


result_3 = sort_price_adv(my_list)
print(f'c)Новый список, отсортированный по убыванию:  {result_3}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    i = 0
    while i < (len(list_in)):
        j = i + 1
        while j < len(list_in):
            if list_in[i] < list_in[j]:
                temp = list_in[j]
                list_in[j] = list_in[i]
                list_in[i] = temp
                j += 1
            else:
                j += 1
        i += 1

    list_out = []
    count_3 = 0
    while count_3 < 5:
        list_out.append(list_in[count_3])
        count_3 += 1
    return list_out


result_4 = check_five_max_elements(my_list)
print(f'd) Список с пятью наибольшими элементами: {result_4}')