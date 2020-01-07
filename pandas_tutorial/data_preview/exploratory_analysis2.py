import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 15)  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 30)  # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비
print(df.head(), '\n')

print("# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인")
print(df.count())
print()

print("# df.count()가 반환하는 객체 타입 출력")
print(type(df.count()))
print()

print("# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인")
unique_values = df['origin'].value_counts()
print(unique_values)
print()

print("# value_counts 메소드가 반환하는 객체 타입 출력")
print(type(unique_values))


