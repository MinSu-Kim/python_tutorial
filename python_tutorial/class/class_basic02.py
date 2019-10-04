class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')


if __name__ == "__main__":
    redcar = Car()
    redcar.drive()
    # redcar.__updateSoftware()  객체에서 직접 접근할 수 없음
    print(dir(redcar))
    redcar._Car__updateSoftware()