class Animal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(self.name + ' walks.')


class Person:
    def __init__(self, name):
        self.__name = name

    def walk(self):
        print(self.__name + ' walks.')


duck = Animal('Duck')
duck.walk()

person = Person('Test')
person.walk()