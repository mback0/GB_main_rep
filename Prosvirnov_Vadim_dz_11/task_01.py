import re


class DataModify:
    def __init__(self, data):
        self.data = data
        pattern = re.compile(r"\d{2}-\d{2}-\d{4}")
        try:
            val_pat = pattern.match(self.data)
            if not val_pat or len(self.data) > 10:
                raise ValueError('Некорректный формат даты')
        except TypeError as err:
            raise TypeError('Передаваемое значение должно быть строкой')


    @classmethod
    def ext_data(cls, obj):
        day = int(obj.data[:2])
        month = int(obj.data[3:5])
        year = int(obj.data[6:])
        return f'День: {day}, Месяц: {month}, Год: {year}'

    @staticmethod
    def validate_data(d, m, y):
        if 0 < int(d) < 32 and 0 < int(m) < 13 and 0 < int(y) < 2023:
            return f'Данные верны'
        else:
            return f'Некорректные данные'


if __name__ == '__main__':
    a = DataModify('25-12-2005')
    #b = DataModify('25-12-222')
    print(a.ext_data(a))
    print(DataModify.validate_data(3, 12, 2016))
    print(DataModify.validate_data(3, 12, 2026))