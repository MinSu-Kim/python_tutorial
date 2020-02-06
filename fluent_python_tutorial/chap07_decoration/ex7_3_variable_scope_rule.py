def f1(a):
    print(a)
    print(b)


# 전역변수
b = 6


def f2(a):
    print(a)
    print(b) #전역변수 b에 접근하지 않고 지역변수 b로 판단하므로 'UnboundLocalError: local variable 'b' referenced before assignment'에러 발생
    b = 9


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__=="__main__":
    f1(3)
    # f2(3)
    f3(3)

    from dis import  dis
    # dis(f1)
    dis(f2)