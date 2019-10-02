def dictionary_exam():
    tel = {'jack': 4098, 'sape': 4139}
    print('type(tel) : ', type(tel), tel)
    tel['guido'] = 4127
    print('추가 ', tel)

    print()
    print("tel['jack'] : ", tel['jack'])

    del tel['sape']
    print("del tel['sape'] => ", tel)

    tel['irv'] = 4127
    print("tel['irv'] = 4127 => ", tel)

    # dictionary to list
    print('type(list(tel)) : ', type(list(tel)), '\n', 'list(tel) : ', list(tel))

    # 키값을 기준으로 정렬
    sorted(tel)
    print('sorted(tel) : ', tel)

    # 키가 딕셔너리에 있는지 검사
    print("'guido' in tel : ", 'guido' in tel)
    print("'jack' not in tel : ", 'jack' not in tel)

    # dict() 생성자는 키-값 쌍들의 시퀀스로 부터 직접 딕셔너리를 구성
    d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print('type(d) : ', d)

    # 딕셔너리 컴프리헨션은 임의의 키와 값 표현식들로 부터 딕셔너리를 만드는데 사용될 수 있음
    x = {x: x ** 2 for x in (2, 4, 6)}
    print(type(x), " : ", x)

    # 키가 간단한 문자열일 때, 때로 키워드 인자들을 사용해서 쌍을 지정하기가 쉬움
    x = dict(sape=4139, guido=4127, jack=4098)
    print(type(x), " : ", x)

    # 딕셔너리로 루핑할 때, items() 메서드를 사용하면 키와 거기에 대응하는 값을 동시에 얻을 수 있음
    for k, v in tel.items():
        print(k , '->', v)

    # 시퀀스를 루핑할 때, enumerate() 함수를 사용하면 위치 인덱스와 대응하는 값을 동시에 얻을 수있음
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    # 둘이나 그 이상의 시퀀스를 동시에 루핑하려면, zip() 함수로 엔트리들의 쌍을 생성
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

    # 시퀀스를 거꾸로 루핑하려면, 먼저 정방향으로 시퀀스를 지정한 다음에 reversed() 함수를 호출
    for i in reversed(range(1, 10, 2)):
        print(i)

    # 정렬된 순서로 시퀀스를 루핑하려면, sorted() 함수를 사용해서 소스를 변경하지 않고도 정렬된 새 리스트를 반환
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)

    # 때로 루프를 돌고 있는 리스트를 변경하고픈 유혹을 느낍니다; 하지만, 종종, 대신 새 리스트를 만드는 것이 더 간단하고 더 안전
    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    print(filtered_data)

    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    print(string1, string2, string3)

    non_null = string1 or string2 or string3
    print(non_null)


if __name__ == "__main__":
    # dictionary_exam()
    res = (1, 2, 3) < (1, 2, 4)
    print(res)
    res = [1, 2, 3] < [1, 2, 4]
    print(res)
    res = 'ABC' < 'C' < 'Pascal' < 'Python'
    print(res)
    res = (1, 2, 3, 4) < (1, 2, 4)
    print(res)
    res = (1, 2) < (1, 2, -1)
    print(res)
    res = (1, 2, 3) == (1.0, 2.0, 3.0)
    print(res)
    res = (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
    print(res)
