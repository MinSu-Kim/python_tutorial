import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 디스플레이 설정 변경
pd.set_option('display.max_columns', len(df.columns))  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', int(df['name'].apply(len).max()))  # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비

print('df.head()', '\n', df.head(), '\n')
# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)  # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)  # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')  # 문자열을 실수형으로 변환

print("# np.histogram 으로 3개의 bin으로 나누는 경계 값의 리스트 구하기")
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

# 3개의 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 으로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],  # 데이터 배열
                      bins=bin_dividers,  # 경계 값 리스트
                      labels=bin_names,  # bin 이름
                      include_lowest=True)  # 첫 경계값 포함

print("# hp_bin 열의 범주형 데이터를 더미 변수로 변환")
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15), '\n')

print("df[['horsepower', 'hp_bin']].head(15)", '\n', df[['horsepower', 'hp_bin']].head(15), '\n')
