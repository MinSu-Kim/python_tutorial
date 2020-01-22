"""
namedtuple()
collections.namedtuple() 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수로서 디버깅할 때 유용
"""

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population, '\n', tokyo[1], '\n', tokyo.coordinates)

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())

[print(key, value, sep=' : ') for key, value in delhi._asdict().items()]

seoul = City('Seoul', 'KR', 6.933, (37.689722, 132.691667))
x = tokyo.__add__(seoul)
print(x, seoul.__contains__('KR'), seoul.count('KR'), seoul.__getitem__(3), seoul.index('KR'))