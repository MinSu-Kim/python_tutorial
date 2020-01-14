lax_coordinates = (33.9435, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) # 튜플 언패킹
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

[print('{}/{}'.format(passport[0], passport[1])) for passport in sorted(traveler_ids)]

print('튜플 언패킹 - %포맷연산자는 튜플을이해하고 각 항목을 하나의 필드로 처리')
[print('%s/%s' % passport) for passport in sorted(traveler_ids)]
print('두 번째 항목을 관심이 없으므로 더비 변수를 나타내는 "_"에 할당')
[print(country) for country, _ in traveler_ids]


#튜플 언패킹 예제
#os.path.split()함수를 이용해서 파일 시스템경로에서 경로명과 파일명을 가져올 수 있다.
import os
_, filename = os.path.split('/home/work/PycharmProjects/python_tutorial/fluent_python_tutorial/chap02_sequence/ex2_1.py')
print(filename)

# *이용한 초과항목 처리
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

print()
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# ^가운데 정렬 https://mkaz.blog/code/python-string-format-cookbook/

fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))