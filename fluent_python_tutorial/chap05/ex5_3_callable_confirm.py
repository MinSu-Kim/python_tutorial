import random

"""
사용자 정의 콜러블형
 파이썬 함수가 실제 객체 일 뿐만 아니라, 모든 파이썬 객체가 함수처럼 동작하게 만들 수 있다.(단 __call__() 인스턴스 메서드구현)
"""


class BingoCage:
    """
    반복 가능 객체를 받아서 그 중 한 항목을 담은 객체를 생성하며, 무작위 순으로 내부에 항목들의 리스트를 저장
    객체를 호출하면 항목을 하나 꺼낸다
    """

    def __init__(self, items):
        self._items= list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoGage')

    def __call__(self):
        return self.pick()


if __name__ == "__main__":
    """
    파이썬에는 다양한 콜러블형이 존재하므로, callable() 내장함수를 사용해서 호출할 수 있는 객체인지 판단하는 방법이 가장 안전
    """
    print(abs, str, 13)
    [print(callable(obj), end=' ') for obj in (abs, str, 13)]
    print()

    bingo = BingoCage(range(3))
    print(bingo.pick(), bingo(), callable(bingo))
    print()