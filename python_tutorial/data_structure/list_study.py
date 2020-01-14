def list_method():
    print("list 메서드", end='\n')
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print("fruits : ", fruits)
    print("fruits.count('apple') : ", fruits.count('apple'))
    print("fruits.count('tangerine') : ", fruits.count('tangerine'))
    print("fruits.index('banana') : ", fruits.index('banana'))
    print("fruits.index('banana', 4) : ", fruits.index('banana', 4))  # Find next banana starting a position 4
    print("fruits.reverse() : ", fruits.reverse())
    print("fruits : ", fruits)
    print("fruits.append('grape') : ", fruits.append('grape'))
    print("fruits : ", fruits)
    print("fruits.sort() : ", fruits.sort())
    print("fruits : ", fruits)
    print("fruits.pop() : ", fruits.pop())


def list_to_stack():
    print("List를 Stack으로", end='\n')
    stack = [3, 4, 5]
    print("stack : ", stack)
    stack.append(6)
    print("stack.append(6) : ", stack)
    stack.append(7)
    print("stack.append(7) : ", stack)
    print()
    print("stack.pop() : ", stack.pop())
    print("stack : ", stack)
    print("stack.pop() : ", stack.pop())
    print("stack : ", stack)
    print("stack.pop() : ", stack.pop())
    print("stack : ", stack)


def list_to_queue():
    print("List를 Queue으로", end='\n')
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    print("queue : ", queue)

    queue.append("Terry")  # Terry arrives
    print('queue.append("Terry") : ', queue)
    queue.append("Graham")  # Graham arrives
    print('queue.append("Graham") : ', queue)

    queue.popleft()  # The first to arrive now leaves
    print("queue.popleft() : ", queue.popleft(), "queue : ", queue)
    queue.popleft()  # The second to arrive now leaves
    print("queue.popleft() : ", queue.popleft(), "queue : ", queue)

    print("queue : ", queue)  # Remaining queue in order of arrival


def list_comprehensions1():
    print("list comprehensions", end='\n')
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print('squars : ', squares)

    squares = list(map(lambda x: x ** 2, range(10)))
    print('squars : ', squares)

    squares = [x ** 2 for x in range(10)]
    print('squars : ', squares)


def list_comprehensions2():
    t = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print("t : ", t)
    print()
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))
    print("combs : ", combs)


def list_comprehensions3():
    vec = [-4, -2, 0, 2, 4]
    print(type(vec), vec)
    # create a new list with the values doubled
    res = [x * 2 for x in vec]
    print(type(res), res)

    # filter the list to exclude negative numbers
    res = [x for x in vec if x >= 0]
    print(type(res), res)

    # apply a function to all the elements
    res = [abs(x) for x in vec]
    print(type(res), res)

    # call a method on each element
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print(type(freshfruit), freshfruit)
    res = [weapon.strip() for weapon in freshfruit]
    print(type(res), res)

    # create a list of 2-tuples like (number, square)
    res = [(x, x ** 2) for x in range(6)]
    print(type(res), res)

    # 튜플은 반드시 괄호로 묶어야 한다. 그렇지 않으면 오류가 발생
    #res = [x, x**2 for x in range(6)]
    #print(type(res), res)

    # flatten a list using a listcomp with two 'for'
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = [num for elem in vec for num in elem]
    print(type(vec), vec)
    print(type(res), res)

    from math import pi
    res = [str(round(pi, i)) for i in range(1, 6)]
    print(type(res), res)


def list_comprehensions4():
    from math import pi
    res = [str(round(pi, i)) for i in range(1, 6)]

    print(type(res), res, end='\n\n')

    for i in range(1, 6):
        print(type(str(round(pi, i))), str(round(pi, i)))

def list_comprehensions5():
    # 길이가 4인 리스트 3개의 리스트로 구현된 3x4 행렬
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print('matrix', matrix)

    # 행과 열을 전치
    transposed = [[row[i] for row in matrix] for i in range(4)]
    print('type(transposed) : ', type(transposed), end='\n')
    print('transposed : ', transposed, end='\n\n')

    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print('transposed : ', transposed, end='\n\n')

    transposed = []
    for i in range(4):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    print('transposed : ', transposed)

    zip_list = list(zip(*matrix))
    print('type(zip_list) : ', type(zip_list), zip_list)
    print('type(zip(*matrix)) : ', type(zip(*matrix)) , zip(*matrix))
    for t in zip(*matrix):
        print(type(t), t)

    # Unpacking Argument Lists
    print(list(range(3, 6)))  # normal call with separate arguments
    args = [3, 6]
    print(list(range(*args)))  # call with arguments unpacked from a list

    # help(zip)

def list_del():
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    print('a : ', a)
    del a[0]
    print('del a[0] : ', a)

    del a[2:4]
    print('del a[2:4] : ', a)

    del a[:]
    print('del a[:] : ', a)

    del a
    print('del a : ', a)


if __name__ == "__main__":
    # list_method()
    # list_to_stack()
    # list_to_queue()
    # list_comprehensions1()
    # list_comprehensions2()
    # list_comprehensions3()
    # list_comprehensions4()
    # list_comprehensions5()
    list_del()