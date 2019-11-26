def mul(a, b):
    c = a * b
    return c


def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)


if __name__ == "__main__":
    x = 10
    y = 20
    add(x, y)

    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    print(type(pairs))
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)
    pairs.sort(key=lambda pair: pair[1], reverse=True)
    print(pairs)
