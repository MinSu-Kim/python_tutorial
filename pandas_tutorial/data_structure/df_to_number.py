import seaborn as sns
import pandas as pd


print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
# 디스플레이 설정 변경
pd.set_option('display.max_columns', 15)  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)  # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비
print(titanic.head())
print(titanic['deck'].describe())

df = titanic.loc[:, ['age', 'fare']]
print(df.head(), type(df), sep='\n')  # 첫 5행만 표시
print()

print("# 데이터프레임에 숫자 10 더하기")
addition = df + 10
print(addition.head(), type(addition), sep='\n')  # 첫 5행만 표시
