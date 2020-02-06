"""
데커레이터
데커레이터된 함수가 정의된 직후에 실행
  - 일반적으로 파이썬이 모듈을 로딩하는 시점(임포트 타임에 실행된다)
"""

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry -> ', registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()