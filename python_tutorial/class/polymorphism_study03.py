from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class SportsCar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar braking!'


class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'


if __name__ == "__main__":
    cars = [Truck('Bananatruck'), Truck('Orangetruck'), SportsCar('Z3')]

    for car in cars:
        print(car.name + ': ' + car.drive())