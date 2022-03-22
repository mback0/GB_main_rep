class MyClass(ValueError):
    msg = 'Введенное значение не является цифрой и не может быть добавлено'


res_list = []
while True:
    try:
        value = input('Введите число: \nДля завершения ввода введите "stop"')
        if value.lower() == 'stop':
            print('\nЗавершение работы программы\n')
            break
        elif not value.isdigit():
            raise MyClass
        else:
            res_list.append(value)

    except MyClass:
        print(MyClass.msg)
    except KeyboardInterrupt:
        print('\nПринудительное завершение работы программы')
        break
print(res_list)
