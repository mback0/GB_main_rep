def get_numbers(src: list):
    res = []
    b = (a for a in src)
    next(b)
    for c in src:
        if src.index(c) != len(src) - 1:
            z = next(b)
            if z > c:
                res.append(z)
    return res


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))