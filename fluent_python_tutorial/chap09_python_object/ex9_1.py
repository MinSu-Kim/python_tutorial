from fluent_python_tutorial.chap09_python_object.Vector2d import Vector2d

if __name__=="__main__":
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)

    x, y = v1
    print(x, y)

    print(v1)

    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)

    print(v1)

    octets = bytes(v1)
    print(octets)

    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))

    print(format(v1))
    print(format(v1, '.2f')) # __format__
    print(format(v1, '.3e'))