import seaborn as sns
import pandas as pd

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 15)  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)  # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비

# titanic 데이터셋 살펴보기
print(titanic.head(), '\n', titanic.info())