class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


if __name__=="__main__":
    x = Gizmo()
    y = Gizmo()

    print(dir())
