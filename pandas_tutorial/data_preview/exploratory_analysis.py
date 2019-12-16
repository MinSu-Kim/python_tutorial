import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print("# 데이터프레임 df의 내용을 일부 확인")
print(df.head(), '\n', df.tail())  # 처음 5개의 행, 마지막 5개의 행

print("# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환")
print(df.shape)
print()

print("# 데이터프레임 df의 내용 확인")
print(df.info())
print()

print("# 데이터프레임 df의 자료형 확인")
print(df.dtypes)
print()

print("# 시리즈(mog 열)의 자료형 확인")
print(df.mpg.dtypes)
print()

print("# 데이터프레임 df의 기술통계 정보 확인")
print(df.describe(), '\n', df.describe(include='all'))
