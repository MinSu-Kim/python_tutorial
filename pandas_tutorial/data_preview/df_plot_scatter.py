import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 한글 설정
matplotlib.rcParams['font.family'] = 'NanumGothicCoding'  # '맑은 고딕'으로 설정,
matplotlib.rcParams['axes.unicode_minus'] = False

# 2개의 열을 선택하여 산점도 그리기
df.plot(x='weight', y='mpg', kind='scatter',
        title='무게(weight)와 연비(mpg)의 관계')

plt.show()
