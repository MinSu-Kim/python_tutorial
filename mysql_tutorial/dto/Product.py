class Product:

    def __init__(self, code=None, name=None, price=None):
        self.__code = code
        self.__name = name
        self.__price = price

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __repr__(self) -> str:
        return '(' + str(self.__code) + ', ' + str(self.__name) + ', ' + str(self.__price) + ')'


if __name__ == '__main__':
    pdt = Product('C001', '라떼', 5000)
    print(str(pdt))

    pdt.code = 'C002'
    pdt.name = '카페라떼'
    pdt.price = 10000
    print(str(pdt))

    ptd2 = Product()
    ptd2.code = 'C003'
    ptd2.name = '아케리카노'
    ptd2.price = 5000
    print(str(ptd2))

    ptd3 = Product()
    print(ptd3, end="\n")

    ptd4 = Product(code='C004')
    print(ptd4)