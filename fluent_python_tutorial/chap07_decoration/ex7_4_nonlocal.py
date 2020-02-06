def make_averager():
    count = 0
    total = 0

    """
    숫자, 문자열, 튜플 등 불변형은 읽을 수 만 있고 값은 갱신 불가능
    count = count + 1 <- 암묵적으로 count는 지역변수를 만듦
    해결책 count를 nonlocal로 선언하면 자유변수임을 나타냄
    """
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))