import numpy as np


def numpy_array01():
    arr_obj = np.array([1, 2, 3, 4, 5])
    print(arr_obj.dtype, arr_obj)


def numpy_array02():
    data2 = [0.1, 5, 4, 12, 0.5]
    arr_obj2 = np.array(data2)  # NumPy의 인자로 정수와 실수가 혼합되어 있을 때 모두 실수로 변환
    print(arr_obj2.dtype, arr_obj2)


def numpy_array03():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(data)


def numpy_arange01():
    data = np.arange(0, 10, 2)
    print(data)
    data = np.arange(1, 10)
    print(data)
    data = np.arange(5)
    print(data)


def numpy_arange02():
    data = np.arange(12).reshape(4, 3) #arange()로 생성되는 배열의 원소개수와 reshape(m, n)의 개수는 같아야 됨
    print(data.shape, data)


def numpy_linspace01():
    data = np.linspace(1, 10, 10)
    print(data)


def numpy_linspace02():
    data = np.linspace(0, np.pi, 20)
    print(data)


def numpy_zeros_ones():
    data = np.zeros(10)
    print(data)
    data = np.zeros((3, 4))
    print(data)
    data = np.ones(10)
    print(data)
    data = np.ones((3,4))
    print(data)


def numpy_eye():
    data = np.eye(3)
    print(data)


if __name__ == '__main__':
    numpy_array01()
    numpy_array02()
    numpy_array03()
    numpy_arange01()
    numpy_arange02()
    numpy_linspace01()
    numpy_linspace02()
    numpy_zeros_ones()
    numpy_eye()