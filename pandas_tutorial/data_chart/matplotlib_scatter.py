import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')  # 스타일 서식 지정

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

cylinders_size = df.cylinders / df.cylinders.max() * 300

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

# axe 객체에 plot 함수로 그래프 출력
ax1.scatter(x=df['weight'], y=df['mpg'], c='coral', s=10)
ax2.scatter(x=df['weight'], y=df['mpg'], c='coral', s=cylinders_size, alpha=0.3)
ax3.stackplot(df['weight'], df['mpg'])
2

# 연비(mpg)와 차중(weight) 열에 대한 산점도 그리기
ax1.set_title('Scatter Plot - mpg vs. weight')
ax2.set_title('Scatter Plot: mpg-weight-cylinders')
ax3.set_title('Scatter Plot: mpg-weight-cylinders')

plt.show()
