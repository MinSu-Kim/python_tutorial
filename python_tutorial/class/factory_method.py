class Car(object):

    def factory(type):
        if type == "RaceCar":
            return RaceCar()
        if type == "Van":
            return Van()

    factory = staticmethod(factory)


class RaceCar(Car):
    def drive(self):
        print("Racecar driving.")


class Van(Car):
    def drive(self):
        print("Van driving.")


if __name__ == '__main__':
    for obj in [Car.factory("RaceCar"), Car.factory("Van")]:
        obj.drive()