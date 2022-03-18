class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def make_order(self, number: int) -> str:
        result = None
        symbol = '*'
        mod = self.cells % number
        fl_div = self.cells // number
        if self.cells < number:
            result = symbol*self.cells
        elif mod == 0:
            val_list = [symbol*number for i in range(int(self.cells / number))]
            result = '\n'.join(val_list)
        else:
            val_list = [symbol * number for i in range(fl_div)]
            val_list.append(symbol*mod)
            result = '\n'.join(val_list)

        return result


    ...  # реализация других магических методов по заданию

    def __add__(self, other):
        if not other.__class__.__name__ == self.__class__.__name__:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        result = self.cells + other.cells
        return Cell(result)

    def __sub__(self, other):
        if not other.__class__.__name__ == self.__class__.__name__:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        result = self.cells - other.cells
        if result < 0:
            raise ValueError('недопустимая операция')
        return Cell(result)

    def __mul__(self, other):
        if not other.__class__.__name__ == self.__class__.__name__:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        result = self.cells * other.cells
        return Cell(result)

    def __truediv__(self, other):
        if not other.__class__.__name__ == self.__class__.__name__:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        result = self.cells // other.cells
        return Cell(result)

    def __floordiv__(self, other):
        if not other.__class__.__name__ == self.__class__.__name__:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        result = self.cells // other.cells
        return Cell(result)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса