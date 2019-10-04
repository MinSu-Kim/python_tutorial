class Human:

    def sayHello(self, name=None):

        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


if __name__ == "__main__":
    obj = Human()
    obj.sayHello()
    obj.sayHello('Guido')

