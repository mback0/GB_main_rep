def main(start, finish):
    with open('bakery.csv', 'r', encoding='utf-8') as prices:
        line = prices.readline()
        count = 1
        while (count <= finish) or (finish == 0 and line):
            if count >= start:
                print(line.strip())
            line = prices.readline()
            count += 1


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        exit(main(1, 0))
    elif len(sys.argv) == 2:
        _, start = sys.argv
        exit(main(int(start), 0))
    elif len(sys.argv) == 3:
        _, start, finish = sys.argv
        exit(main(int(start), int(finish)))
    else:
        print('Неверное количество аргументов')

