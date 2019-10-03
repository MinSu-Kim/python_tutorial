# Function defined outside the class
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


if __name__ == "__main__":
    c = C()
    print('c.g() => ', c.g())
    print('c.h() => ', c.h())
    print('c.f => ', c.f(1,2))
