class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


def make_averager():
    series = [] # 지역변수가 아니고 자유변수(free variable) 지역범위에 바인딩되지 않은 변수

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == "__main__":
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    # maker_average()로 생성한 함수 조사하기
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__, avg.__closure__[0].cell_contents, sep='\n')