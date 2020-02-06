if __name__== "__main__":
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print(lewis is charles)

    print(id(charles), id(lewis), sep='\n')

    lewis['balance'] = 950
    print(charles)

    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    print(alex)
    print(alex == charles)
    print(alex is not charles)
