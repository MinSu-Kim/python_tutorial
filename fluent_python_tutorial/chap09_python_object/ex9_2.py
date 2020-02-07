import math
from array import array


class Vector2d:
    __slots__ = ('__x', '__y')

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))# self.x(self), self.y(self)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


if __name__ == "__main__":
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)

    print(hash(v1), hash(v2))
    print(set([v1, v2]))

    # print(v1.__dict__, v1._Vector2d__x, sep='\n')
    print(v1.__slots__)