from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        m_len = len(matrix[0])
        for x in matrix:
            if len(x) != m_len:
                raise ValueError('fail initialization matrix')
            self.matrix = matrix

    def __str__(self):
        res_list = []
        for lists in self.matrix:
            temp_list = []
            for el in lists:
                temp_list.append(str(el))
            res_str = ' '.join(temp_list)
            res_list.append(f'| {res_str} | ')
        return '\n'.join(res_list)

    def __add__(self, other):
        matrix_sum = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(matrix_sum)

if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print('\n')
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    #fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """