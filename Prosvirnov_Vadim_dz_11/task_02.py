class CatchZero(ZeroDivisionError):
    def __init__(self, value):
        self.value = value

    def zero_catch(self, other, operator='/'):
        res = None
        try:
            if operator == '/':
                res = self.value / other.value
            elif operator == '//':
                res = self.value // other.value
            elif operator == '%':
                res = self.value % other.value
        except ZeroDivisionError as err:
            res = f'При выполнении операции деления произошла ошибка: {err}.\nПопробуйте указать другой делитель'
        return res

    def __truediv__(self, other):
        return self.zero_catch(other, operator='/')

    def __floordiv__(self, other):
        return self.zero_catch(other, operator='//')

    def __mod__(self, other):
        return self.zero_catch(other, operator='%')


if __name__ == '__main__':
    a = CatchZero(25)
    b = CatchZero(5)
    c = CatchZero(0)
    print(a / b)
    print(a / c)
    print(b // a)
    print(b // c)
    print(a % b)
    print(a % c)
