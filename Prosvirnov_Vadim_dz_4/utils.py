import requests
import requests.utils


def val_from_tag(url: str = 'http://www.cbr.ru/scripts/XML_daily.asp', tag: str = 'CharCode'):


    resp = requests.get(url)
    text = resp.text

    result = []
    a = text.find(f'<{tag}>')
    b = text.find(f'</{tag}>')
    c = text[a + len(tag) + 2:b]
    result.append(c)

    while a != -1 and b != -1:
        a = text.find(f'<{tag}>', b)
        b = text.find(f'</{tag}>', a)
        if a != -1 and b != -1:
            c = text[a + len(tag) + 2:b]
            result.append(c)

    return result

charcodes = val_from_tag(tag='CharCode')
nominals_str = val_from_tag(tag='Nominal')
values_str = val_from_tag(tag='Value')

values = []
nominals = []
for z in values_str:
    x = float(z.replace(",", "."))
    values.append(x)
for x in nominals_str:
    i = int(x)
    nominals.append(i)


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    if charcodes.count(code):
        idx_codes = charcodes.index(code)
        result_value = values[idx_codes] / nominals[idx_codes]
        return result_value
    else:
        return None
