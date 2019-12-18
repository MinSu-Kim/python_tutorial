import pandas as pd

df = pd.read_csv('stock-data.csv')
print(df.head(), '\n', df.info(), '\n')

# 문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   #df에 새로운 열로 추가

print("# 문자열 데이터(시리즈 객체)를 판다스 Timestamp로 변환 및 데이터 내용 및 자료형 자료형 확인")
print(df.head(), '\n', df.info(), '\n', type(df['new_Date'][0]), '\n')

# 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제
df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)

print("# 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제, 데이터 내용 및 자료형 자료형 확인")
print(df.head(), '\n', df.info())
