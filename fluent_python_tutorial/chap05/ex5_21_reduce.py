from functools import reduce
from operator import mul, itemgetter


def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


def fact2(n):
    return reduce(mul, range(1, n+1))


if __name__=="__main__":
    print(fact(5))

    f = lambda a, b: a*b
    print(f(3, 5))

    n = 5
    r = reduce(f, range(1, n+1)) # ((((1 * 2) * 3) * 4) * 5)
    print(r)

    print(fact2(5))

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    [print(city) for city in sorted(metro_areas, key=itemgetter(1))] # 국가 코드으로 정렬

    cc_name = itemgetter(1, 0)
    [print(cc_name(city)) for city in metro_areas]