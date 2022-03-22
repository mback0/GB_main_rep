class Cpx:
    def __init__(self, a, b, i):
        self.a = a
        self.b = b
        self.z = a + b * i
        self.i = i

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        n_i_1 = self.a * other.b * other.i
        n_i_2 = self.b * self.i * other.a
        sqr = self.b * other.b
        return f'z = {self.a * other.a - sqr} + {n_i_1 + n_i_2}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


if __name__ == '__main__':

    z1 = Cpx(1, 3, 1)
    z2 = Cpx(2, 1, 1)
    print(z1)
    print(z1 + z2)
    print(z1 * z2)

