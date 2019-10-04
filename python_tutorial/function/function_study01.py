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
