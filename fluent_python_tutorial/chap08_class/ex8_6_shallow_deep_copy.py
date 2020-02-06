import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passensers = []
        else:
            self.passensers = list(passengers)

    def pick(self, name):
        self.passensers.append(name)

    def drop(self, name):
        self.passensers.remove(name)

    def __repr__(self) -> str:
        return str(self.passensers)


if __name__ == "__main__":
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3), sep='\n')

    print(bus1, bus2, bus3, sep='\n')
    bus1.drop('Bill')
    print(bus1, bus2, bus3, sep='\n')

    print()
    a = [10, 20]
    b = [a, 30]
    print(a)
    a.append(b)
    print(a)

    from copy import deepcopy
    c = deepcopy(a)
    print(c)