if __name__ == "__main__":
    """
    기본 복사는 얕은 복사(shallow copy)
    """
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])

    print(t1 == t2)
    print(id(t1[-1]))

    t1[-1].append(99)
    print(t1)
    print(id(t1[-1]))
    print(t1 == t2)

    print()
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)
    print(l1, l2, sep='\n')

    l1.append(100)
    print('l1:', l1)
    print('l2:', l2)

    l1[1].remove(55)
    print('l1:', l1)
    print('l2:', l2)

    l2[1] += [33, 22]
    l2[2] += (10, 11)
    print('l1:', l1)
    print('l2:', l2)
