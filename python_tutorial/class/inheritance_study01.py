class ParentClass():
    def __init__(self):
        print('ParentClass')

    def parent_method(self):
        print('parent_method()')


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print('ChildClass')

    def parent_method(self):
        print('override method')


if __name__ == "__main__":
    p = ParentClass()
    c = ChildClass()

    p.parent_method()
    c.parent_method()

    if isinstance(c, ChildClass):
        print('c isChildClass')
    else:
        print('c unChildClass')

    if isinstance(c, ParentClass):
        print('c isParentClass')
    else:
        print('c unParentClass')

    if isinstance(p, ChildClass):
        print('p isChildClass')
    else:
        print('p unChildClass')

    if isinstance(p, ParentClass):
        print('p isParentClass')
    else:
        print('p unParentClass')

    if issubclass(ChildClass, ParentClass):
        print('ChildClass is ParentClass SubClass')