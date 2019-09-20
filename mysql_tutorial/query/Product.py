class Product:
    def __init__(self, code=None, name=None):
        self.__code = code
        self.__name = name

    @property
    def code(self):  # getter
        return self.__code

    @code.setter
    def code(self, code):  # setter
        self.__code = code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __repr__(self) -> str:
        return '(' + str(self.__code) + ', ' + str(self.__name) + ')'


if __name__ == '__main__':
    pdt = Product('C001', '라떼')
    print(pdt)

    pdt.code = 'C002'
    pdt.name = '카페라떼'
    print(pdt)

    ptd2 = Product()
    ptd2.code = 'C003'
    ptd2.name = '아케리카노'
    print(str(ptd2))

    ptd3 = Product()
    print(ptd3, end="\n")

    ptd4 = Product(code='C004')
    print(ptd4)