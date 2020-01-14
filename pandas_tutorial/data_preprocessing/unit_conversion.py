import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 30)  # 출력할 열의 너비
pd.set_option('display.width', 640)  # 콘솔 출력 너비

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']
print(df.head(3), '\n')




print("# mpg(mile per gallon)를 kpl(kilometer per liter)로 변환 (mpg_to_kpl = 0.425)")
mpg_to_kpl = 1.60934 / 3.78541

print("# mpg 열에 0.425를 곱한 결과를 새로운 열(kpl)에 추가")
df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head(3), '\n')

print("# kpl 열을 소수점 아래 둘째 자리에서 반올림 ")
df['kpl'] = df['kpl'].round(2)
print(df.head(3))
