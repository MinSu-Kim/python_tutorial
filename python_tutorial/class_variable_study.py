class Car():
    """A Simple Class"""   # 첫줄에 선언해야 __doc__ 속성에 저장됨
    instance_count = 0     # 클래스변수

    def __init__(self, size, color):
        self.size = size      # 인스턴스 변수
        self.__color = color  # private 인스턴스 변수
        Car.instance_count = Car.instance_count + 1

    def move(self):
        print("자동차({} & {})가 움직입니다.".format(self.size, self.__color))

    def set_color(self, color):
        self.__color = color

    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수: {}".format(cls.instance_count))

    @staticmethod
    def check_type(model_code):
        if model_code >= 20:
            print("이 자동차는 전기차입니다.")
        elif 10 <= model_code < 20:
            print("이 자동차는 가솔린차입니다.")
        else:
            print("이 자동차는 디젤차입니다.")

    def __str__(self) -> str:
        return "자동차정보 : 사이즈 {} 컬러 {}".format(self.size, self.__color)


if __name__ == "__main__":

    car_lists = []
    car_sizes = [25, 35]
    car_colors = ["red", "black"]

    Car.count_instance()
    for size, color in zip(car_sizes, car_colors):
        car_lists.append(Car(size, color))
        Car.count_instance()

    for car in car_lists:
        print(car)
        car.move()
        print(Car.__doc__)

    Car.check_type(35)


