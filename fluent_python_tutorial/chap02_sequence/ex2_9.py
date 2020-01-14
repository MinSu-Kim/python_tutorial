"""
namedtuple()
collections.namedtuple() 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수로서 디버깅할 때 유용
"""

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population, '\n', tokyo[1], '\n', tokyo.coordinates)