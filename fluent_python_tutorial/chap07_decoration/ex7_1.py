def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


if __name__ == "__main__":
    target = deco(target)   # target()함수를 deco로 데커레이트함
    target()                # target함수가 inner()함수로 대체
    print(target)

