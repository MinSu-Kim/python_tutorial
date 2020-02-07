from fluent_python_tutorial.chap11_ABC.tombola import Tombola


class Fake(Tombola):

    def pick(self):
        return 13


if __name__=="__main__":

    Fake
    f = Fake()# Can't instantiate abstract class Fake with abstract methods load