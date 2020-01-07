import numpy as np
from scipy import stats

data = np.array([4, 5, 1, 2, 7, 2, 6, 9, 3])

print('평균 계산')
dt_mean = np.mean(data)
print("Mean : ", round(dt_mean, 2))

print('중간값 계산')
dt_median = np.median(data)
print("Meditan : ", dt_median)

print('최빈값 계산')
dt_mode = stats.mode(data)
print(type(dt_mode))
print('Mode : ', dt_mode[0][0])