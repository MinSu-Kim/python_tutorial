class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


if __name__ == "__main__":
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')

    print(d.tricks)
    print(e.tricks)