def plus_int(x):
    msg = f'wrong val {x}'
    if type(x) == int:
        if x < 0:
            raise ValueError(msg)
    else:
        raise ValueError(msg)

def val_checker(func):
    def decor(func_2):
        def wrapper(*args):
            func(*args)
            return func_2(*args)
        return wrapper
    return decor

@val_checker(plus_int)
def calc_cube(x):
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
