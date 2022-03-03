def decor(func):
    def wrap(*args, **kwargs):
        val_in_args = [f'{i}: {type(i)}' for i in args]
        print(', '.join(val_in_args))
        val_in_kwargs = [f'{i} = {z}: {type(z)}' for i, z in kwargs.items()]
        print(', '.join(val_in_kwargs))
        val_out = func(*args, **kwargs)
        return val_out
    return wrap

@decor
def calc_cube(*args, **kwargs):
    res_list = [x**3 for x in args]
    return res_list


print(calc_cube(5, 10, 25, abc='5'))
