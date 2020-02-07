from fluent_python_tutorial.chap11_ABC.tombola import Tombola
from fluent_python_tutorial.chap11_ABC.tombolist import TomboList

if __name__=="__main__":
    res = issubclass(TomboList, Tombola)
    print(res)
    t = TomboList(range(100))
    res = isinstance(t, Tombola)
    print(res)

    print(TomboList.__mro__)