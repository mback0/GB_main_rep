from abc import ABC, abstractmethod
import random


class OfficeEquipment(ABC):
    def __init__(self, manufacturer, model, status=False):
        self.manufacturer = manufacturer
        self.model = model
        self.status = status

    @abstractmethod
    def get_info(self):
        pass

    def is_broken(self):
        self.status = True

    @abstractmethod
    def nameof(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, status=False):
        super().__init__(manufacturer, model, status=False)

    def get_info(self):
        return f'Оборудование Принтер, производитель: {self.manufacturer}, модель: {self.model}'

    def is_broken(self):
        self.status = True

    def nameof(self):
        return f'Принтеры'


class Scaner(OfficeEquipment):
    def __init__(self, manufacturer, model, status=False):
        super().__init__(manufacturer, model, status=False)

    def get_info(self):
        return f'Оборудование Сканер, производитель: {self.manufacturer}, модель: {self.model}'

    def nameof(self):
        return f'Сканеры'


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, model, status=False):
        super().__init__(manufacturer, model, status=False)

    def get_info(self):
        return f'Оборудование Ксерокс, производитель: {self.manufacturer}, модель: {self.model}'

    def nameof(self):
        return f'Ксероксы'


class WareHouse:
    def __init__(self):
        self.subdivisions = []
        self.content = {}
        self.equip_dict = {'Принтеры': Printer, 'Сканеры': Scaner, 'Ксероксы': Xerox}
        self.inv_numbers = [x for x in range(10**5, 10**6)]
        self.content_by_type = {'Принтеры': 0, 'Сканеры': 0, 'Ксероксы': 0}

    def to_add(self, equip_type, manufacturer, model, amount=1):
        self.content_by_type[equip_type] += amount
        for _ in range(amount):
            eq_code = random.choice(self.inv_numbers)
            self.inv_numbers.remove(eq_code)
            temp_dict = {self.equip_dict[equip_type](manufacturer, model): eq_code}
            self.content.update(temp_dict)
        print(f'На склад поступило {amount} единиц техники {equip_type}')

    def to_remove(self, equip_type, amount=1):
        if not isinstance(amount, int) or amount <= 0:
            print('Некорректно указано количество единиц для списания со склада')
        elif amount > self.content_by_type[equip_type]:
            print(f'На складе в данный момент {self.content_by_type[equip_type]} единиц оборудования {equip_type}. Укажите меньшее число единиц')
        else:
            print(f'Склад лишился {amount} единиц техники {equip_type}')
            self.content_by_type[equip_type] -= amount
            while not amount == 0:
                for k, v in self.content.items():
                    if k.nameof() == equip_type:
                        self.content.pop(k)
                        self.inv_numbers.append(v)
                        amount -= 1
                        break


    def show_all(self):
        print('Инвентаризация: ')
        for keys, objects in self.content.items():
            if keys.is_broken():
                self.to_remove(keys.nameof())
                print(f'{keys.get_info} вышел из строя и списан со склада')
            print(f'{keys.get_info()}, серийный номер: {objects}')

    def show_all_by_type(self):
        print(self.content_by_type)


if __name__ == '__main__':
    wh = WareHouse()
    wh.to_add('Принтеры', 'Canon', 'LBP-420', 5)
    wh.to_add('Сканеры', 'Samsung', 'DP440', 1)
    wh.to_add('Сканеры', 'Samsung', 'S2', 2)
    wh.to_add('Ксероксы', 'Xerox', 'V12', 3)
    wh.show_all_by_type()
    wh.to_remove('Сканеры', 4)
    wh.to_remove('Сканеры', 3)
    wh.show_all_by_type()
    wh.show_all()
