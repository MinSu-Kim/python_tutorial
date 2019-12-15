import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print()

pd.options.mode.chained_assignment = None  # 경고를 안전하게 비활성화 default='warn'

print("inplace=False", " pd.options.mode.chained_assignment = None")
# 데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 행(row)을 삭제
df2 = df[:]

df3 = df2.drop('우현')
print("df4", df3, sep='\n')
print()

# 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row)을 삭제
df4 = df[:]
df5 = df4.drop(['우현', '인아'], axis=0)
print("\ndf5", df5, sep='\n')
print()

# inplace = True
print("inplace=True", "pd.options.mode.chained_assignment = 'warn'")
pd.options.mode.chained_assignment = 'warn'
df.drop('인아', inplace=True)
print("df", df, sep='\n')

df.drop(['서준', '우현'], axis=0, inplace=True)
print("\ndf", df, sep='\n')