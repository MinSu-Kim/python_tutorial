def set_exam01():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print('basket : ', basket)  # show that duplicates have been removed
    print("'orange' in basket : ", 'orange' in basket)  # fast membership testing
    print("'crabgrass' in basket : ", 'crabgrass' in basket)

    print('\n')
    # Demonstrate set operations on unique letters from two words
    a = set('abracadabra')
    print('a : ', a)  # unique letters in a
    b = set('alacazam')
    print('b : ', b)

    print('a - b : ', a - b)  # letters in a but not in b
    print('a | b : ', a | b)  # letters in a or b or both
    print('a & b : ', a & b)  # letters in both a and b
    print('a ^ b : ', a ^ b)  # letters in a or b but not both

    # 집합 컴프리헨션도 지원
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print("{x for x in 'abracadabra' if x not in 'abc'} : ", a)


if __name__ == "__main__":
    set_exam01()