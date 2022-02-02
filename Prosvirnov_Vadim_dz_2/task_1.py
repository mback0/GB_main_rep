import types

exp_1 = 15 * 3
exp_2 = 15 / 3
exp_3 = 15 // 2
exp_4 = 15 ** 2

val_list = [exp_1, exp_2, exp_3, exp_4]
type_list = [int, float, str, bool, set, tuple, range, list, dict, types.FunctionType]

for x in val_list:
    for i in type_list:
        if isinstance(x, i) == True:
            print(f'Результат выражения относится к {i}')