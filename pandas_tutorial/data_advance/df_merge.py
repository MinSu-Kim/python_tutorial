import pandas as pd

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 15)  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)  # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비

print("# 주식 데이터를 가져와서 데이터프레임 만들기")
df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')
print("df1", '\n')
print(df1, '\n')
print()
print('df2', '\n')
print(df2, '\n')

print("# 데이터프레임 합치기 - 교집합")
merge_inner = pd.merge(df1, df2)
print(merge_inner, '\n')

print("# 데이터프레임 합치기 - 합집합")
merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer, '\n')

print("# 데이터프레임 합치기 - 왼쪽 데이터프레임 기준, 키 값 분리")
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
print(merge_left, '\n')

print("# 데이터프레임 합치기 - 오른쪽 데이터프레임 기준, 키 값 분리")
merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(merge_right, '\n')

print("# 불린 인덱싱과 결합하여 원하는 데이터 찾기")
price = df1[df1['price'] < 50000]
print(price.head(), '\n')

value = pd.merge(price, df2)
print(value)
