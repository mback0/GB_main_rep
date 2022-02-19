def main(argv):
    _, price = argv
    with open('bakery.csv', 'a', encoding='utf-8') as prices:
        prices.write(f'{price}\n')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        exit(main(sys.argv))
    else:
        print('Неверное число аргументов')