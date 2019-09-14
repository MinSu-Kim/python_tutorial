import numpy as np


def numpy_state_operator():
    data = np.arange(5)
    print('data=', data, 'data[0:5] =' , data[0:5], 'data[1:5]=', data[1:5])
    print('배열의 합 {0} 배열의 평균 {1}'.format(data.sum(), data.mean()))
    print('표준편차 {0}, 분산{1}'.format(data.std(), data.var()))
    print('최소값 {0}, 최대값 {1}'.format(data.min(), data.max()))
    print('누적합[0:5] {0}, 누적곲[1:5] {1}'.format(data.cumsum(), data[1:5].cumprod()))


def numpy_matrix_operator():
    a = np.arange(4).reshape(2, 2)
    b = np.array([3, 2, 0, 1]).reshape(2,2)
    print('a = ', a, '\n', 'b = ', b)
    print('행렬 곱 a * b ', a.dot(b))
    print('행렬 곱 a * b ', np.dot(a, b))

    print('전치 행렬 ', np.transpose(a))
    print('전치 행렬 ', a.transpose())

    print('역행렬 ', np.linalg.inv(a))
    print('행렬식 ', np.linalg.det(a))


if __name__ == '__main__':
    numpy_state_operator()
    numpy_matrix_operator()