import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count: int) -> list:
    ns, adv, adj = random.choices(nouns, k=count), random.choices(adverbs, k=count), random.choices(adjectives, k=count)
    a = zip(ns,adv,adj)
    list_out = []
    for i in a:
        str_out = " ".join(i)
        list_out.append(str_out)

    return list_out

print(get_jokes(2))


def get_jokes_adv(count: int = 1, flag: bool = True) -> list:
    """""
    Генерирует предложения, сформированные из трех случайных слов, взятых из трех списков.
    Принимает два аргумента:
    count -- число сформированных предложений, не может быть больше длины списков (default = 1)
    flag -- флаг, отвечающий за повтор слов в предложениях, true - слова в шутках могут повторяться, false - одно слова встречается один раз (default - True)   
    """""
    if count <= len(nouns) and len(adverbs) and len(adjectives):
        result = []
        if flag == True:
            result = get_jokes(count)
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(count):
                result.append(nouns.pop() + ' ' + adverbs.pop() + ' ' + adjectives.pop())
        return result
    else:
        print('Переданное число слишком велико')
print(get_jokes_adv(count = 5, flag = False))






