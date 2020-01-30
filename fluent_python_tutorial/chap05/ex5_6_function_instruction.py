from math import factorial

if __name__ == "__main__":
    print(dir(factorial))

    class C: pass       # 기본적인 사용자 정의 클래스 생성
    obj = C()           # C클래스의 객체 생성
    def func(): pass    # 기본적인 함수를 생성

    # 뺄셈연산을 이용하여 함수에는 존재하지만 기본 클래스에는 존재하지 않는 속성을 나열
    [print(attr) for attr in sorted( set(dir(func)) - set(dir(obj)) )]

    """
    일반적인 사용자 정의 클래스의객체와 마찬가지로 함수는 __dict__ 속성을 이용해서 객체에 할당된 사용자 속성을 보
    """