import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print("df", df, sep='\n')
print()

pd.options.mode.chained_assignment = None  # 경고를 안전하게 비활성화 default='warn'
print("inplace=False", " pd.options.mode.chained_assignment = None")

# 데이터프레임 df를 복제하여 변수 df4에 저장. df4의 1개 열(column)을 삭제
df4 = df[:]
sub_df4 = df4.drop('수학', axis=1)
print("sub_df4", sub_df4, sep='\n')
print('\n')

# 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 2개 열(column)을 삭제
df5 = df[:]
sub_db5 = df5.drop(['영어', '음악'], axis=1)
print("sub_db5", sub_db5, sep='\n')

pd.options.mode.chained_assignment = 'warn'  # 경고를 안전하게 비활성화 default='warn'
print("inplace=True", " pd.options.mode.chained_assignment = 'warn'")

# df(원본객체)의 1개 열(column)을 삭제
df.drop('수학', axis=1, inplace=True)
print("df", df, sep='\n')
print('\n')

# df(원본객체)의 2개 열(column)을 삭제
df.drop(['영어', '음악'], axis=1, inplace=True)
print("df", df, sep='\n')
