import numpy as np


def typecast01():
    data = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
    print(data, data.dtype) # <U8 Unicode 문자수는 최대8개
    cast_data = data.astype(float)
    print(cast_data, cast_data.dtype)

    str_data = np.array(['1', '2', '3', '4'])
    print(str_data, str_data.dtype)
    int_data = str_data.astype(int)
    print(int_data, int_data.dtype)

    int_data = cast_data.astype(int)
    print(int_data, int_data.dtype)


def rnd():
    rnd_num = np.random.rand(2, 3) #2행3열 0~1까지의 난수생성
    print(rnd_num)

    rnd_num = np.random.rand()
    print(rnd_num)

    rnd_num = np.random.randint(10, size=(3,4)) #정수로 난수 배열 생성
    print('3행 4열의 임의의 난수 배열 생성', rnd_num)

    rnd_num = np.random.randint(1, 45, size=6)
    print('1~44까지의 임의의 정수 생성', rnd_num)


def array_operation():
    arr1 = np.array([10, 20, 30, 40])
    arr2 = np.array([1, 2, 3, 4])
    print(arr1 * arr2)
    print(arr1 - arr2)
    print(arr1 / arr2)
    print(arr1 + arr2)
    print(arr2 * 2)
    print(arr2 ** 2)
    print(arr1 > 20)


if __name__ == '__main__':
    typecast01()
    rnd()
    array_operation()