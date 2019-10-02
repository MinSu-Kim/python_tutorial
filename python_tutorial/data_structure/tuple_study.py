def tuple_exam01():
    t = 12345, 54321, 'hello!'
    print('type(t) : ', type(t), 't : ', t, end='\n')
    print('t[0] : ', t[0], 'type(t[0) : ', type(t[0]), end='\n\n')


    # Tuples may be nested:
    u = t, (1, 2, 3, 4, 5)
    print('type(u) : ', type(u), 'u : ', u, end='\n\n')

    # Tuples are immutable:
    # t[0] = 88888

    # but they can contain mutable objects:
    v = ([1, 2, 3], [3, 2, 1])
    print('type(v) : ', type(v), 'v: ', v, end='\n')
    for s in v:
        print('type(s) : ', type(s), s)

    print()
    empty = ()
    singleton = 'hello',  # <-- note trailing comma
    print('len(empty) : ', len(empty))
    print('len(singleton) : ', len(singleton))
    print('singleton : ', singleton)

    # tuple packing
    t = 12345, 54321, 'hello!'
    # tuple unpacking
    x, y, z = t
    print('x, y, z : ', x, y, z)

if __name__ == "__main__":
    tuple_exam01()