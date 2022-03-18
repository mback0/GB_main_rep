class Clothes: ...


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calculate(self):
        return round((self.size/6.5 + 0.5), 2)


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def calculate(self):
        return round((2*self.height + 0.3), 2)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3