class Car:
    def __init__(self):
        self.__horsepower = 100

    @property
    def horsepower(self):               # getter
        return self.__horsepower

    @horsepower.setter
    def horsepower(self, horsepower):   # setter
        self.__horsepower = horsepower

    def __repr__(self) -> str:
        return 'horsepower {0}'.format(self.__horsepower)


class MyClass(object):
    def __init__(self, *args, **kwargs):
        # args   -- 이름이 없는 인자를 저장하는 tuple
        # kwargs -- 이름이 있는 인자를 저장하는 dict
        # (*args, **kwargs)를 쓸 때에는 이름이 없는 인자를 먼저, 이름이 없는 인자를 나중에 써야 합니다.
        print("aargs:", args)
        print("kwargs:", kwargs)
        if kwargs['num'] is None:
            num = 1
        else:
            num = kwargs['num']
        print("num", num)


class MyClass2(object):
    def __init__(self, num='test'):
        self.__num=num

    def __repr__(self) -> str:
        return self.__num


if __name__ == '__main__':
    car = Car()
    # car.__horsepower invisible
    print(car.horsepower)
    print(str(car)) # __repr__(self) 호출
    print(car)      # __repr__(self) 호출
    car.horsepower = 111  # setter 호출
    print(car.horsepower)  # getter 호출

    print()
    MyClass(3, "hello", num=1, mystring="mystring")

    print()
    o = [MyClass2(), MyClass2('aaa')]
    for t in o:
        print(t)