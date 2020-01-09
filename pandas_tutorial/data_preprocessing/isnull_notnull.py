import seaborn as sns
import pandas as pd

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 16)  # 출력할 최대 열의 개수
pd.set_option('display.width', 600)  # 콘솔 출력 너비

print(df.head(), '\n')
print(df.info(), '\n')

print("# deck 열의 NaN 개수 계산하기")
nan_deck = df['deck'].value_counts(dropna=False) 
print(nan_deck, '\n')

print("# isnull() 메서드로 누락 데이터 찾기")
print(df.head().isnull(), '\n')

print("# notnull() 메서드로 누락 데이터 찾기")
print(df.head().notnull(), '\n')

print("# isnull() 메서드로 누락 데이터 개수 구하기")
print(df.head().isnull().sum(axis=0))

