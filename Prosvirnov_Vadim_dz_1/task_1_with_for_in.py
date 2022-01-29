def convert_time(duration: int):
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = ((duration % 86400) % 3600) // 60
    sec = ((duration % 86400) % 3600) % 60

    if duration >= 86400:
        res = "{} дн {} час {} мин {} сек".format(days, hours, minutes, sec)

    elif 86400 > duration and duration >= 3600:
        res = "{} час {} мин {} сек".format(hours, minutes, sec)

    elif 3600 > duration and duration >= 60:
        res = "{} мин {} сек".format(minutes, sec)

    else:
        res = "{} сек".format(sec)

    return res

my_list = [56230, 4123245, 235, 4342, 912540]
for duration in my_list:
    result = convert_time(duration)
    print('Значение {} сек равно {}'.format(duration, result))