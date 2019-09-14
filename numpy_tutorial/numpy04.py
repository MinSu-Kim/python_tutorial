import numpy as np

#배열의 인덱싱과 슬라이싱
#인덱싱(배열의 위치나 조건을 지정하여 배열의 원소를 선택하는 것
#슬라이싱(범위를 지정해 배열의 원소를 선택하는 것


def array_index():
    data = np.arange(0, 50, 10)
    print(data)
    print(data[0], data[4])
    data[4] = 70
    print(data)
    print(data[[1, 3, 4]])

    data2 = np.arange(10, 100, 10).reshape(3, 3)
    print(data2)
    print(data2[1])
    print(data2[2,2])
    data2[2]=np.array([50, 51, 52])
    print(data2)

    print(data2[[0, 2], [0, 1]])
    print(data2[data2 > 50])
    print(data2[(data2 % 2 == 0)])


def array_slicing():
    print('array_slicing')
    data = np.arange(10, 100, 10).reshape(3,3)
    print(data)
    print(data[1:3, 1:3])
    print(data[1:, 1:])


if __name__ == '__main__':
    array_index()
    array_slicing()