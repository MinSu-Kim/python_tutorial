def dan(num):
    for i in range(1, 10):
        print('{0} * {1} = {2:2}'.format(num, i, num*i))


def gugudan():
    for dan in range(2,10):
        for i in range(1,10):
            print('{0} * {1} = {2:2}'.format(dan, i, dan * i))


def gugudan2():
    for i in range(1, 10):
        for dan in range(2, 10):
            print('{0} * {1} = {2:2}'.format(dan, i, dan * i), end='\t')
        print()


if __name__ == "__main__":
    dan(2)
    gugudan()
    gugudan2()