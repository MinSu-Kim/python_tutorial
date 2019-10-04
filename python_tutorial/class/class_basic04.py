class Car:
    __max_speed = 0
    __name = ""

    def __init__(self):
        self.__max_speed = 200
        self.__name = "Supercar"

    def drive(self):
        print(self.__name + ' driving. maxspeed ' + str(self.__max_speed))

    def setMaxSpeed(self, speed):
        self.__max_speed = speed


if __name__ == "__main__":
    red_car = Car()
    red_car.drive()
    red_car.setMaxSpeed(320)
    red_car.drive()