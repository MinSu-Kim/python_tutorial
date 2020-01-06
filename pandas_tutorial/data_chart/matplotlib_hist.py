import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')  # 스타일 서식 지정
# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df['mpg'].value_counts())

import numpy as np
count, bin_divider = np.histogram(df['mpg'], bins=10)
[print(c, d) for c, d in zip(count, bin_divider)]

# 연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()
