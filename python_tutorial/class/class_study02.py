class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


def prn_dog_info(dog):
    print('kind : {},  name : {}'.format(dog.kind, dog.name))


if __name__ == "__main__":
    d = Dog('Fido')
    e = Dog('Buddy')

    prn_dog_info(d)
    prn_dog_info(e)
