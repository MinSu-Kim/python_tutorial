class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


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