import pandas as pd
import numpy as np

data = {'제품': ['사과', '딸기', '수박'],
        '가격': [1800, 1500, 3000],
        '판매량': [24, 38, 13]}
df = pd.DataFrame(data)
df = df.set_index(['제품'])
print(df)

print(df.describe())

print(df.가격.mean())
print(df.판매량.mean())

data2 = {'x': np.arange(1, 6),
         'y': np.arange(2, 11, 2)}
df2 = pd.DataFrame(data2)
print(df2)

data3 = {'col1': np.arange(1, 6),
         'col2': ['a', 'b', 'c', 'd', 'e'],
         'col3': np.arange(6, 11)}
df3 = pd.DataFrame(data3)
print(df3)

s = pd.Series({'scott': 3000})
print(s)
s.scott = s.scott * 2
print(s)

s2 = pd.Series({'scott': [100, 200, 300]})
print(s2)

data = {'제품': ['사과', '딸기', '수박'],
        '가격': [1800, 1500, 3000],
        '판매량': [24, 38, 13]}
df = pd.DataFrame(data)
print(df)

print(df.가격.mean(), '\n', df.판매량.mean())
df = df.replace({'가격': 1500}, {'가격': 2000})
print(df)

df['총판매액'] = df.가격 * df.판매량
print(df)

data = {'시험': ['중간', '기말'],
        '수학': [95, 90],
        '국어': [90, 85],
        '영어': [85, 80]}
exam = pd.DataFrame(data)
exam = exam.set_index(['시험'])
# 과목별 평균 및 합계
print(exam, '\n', exam.sum(), '\n', exam.mean())

s_name = pd.Series(['Potter', 'Elsa', 'Gates', 'Wendy', 'Ben'], name='name')
s_gender = pd.Series(['Female', 'Male', 'Female', 'Male', 'Female'], name='gender')
s_math = pd.Series([85, 76, 99, 88, 40], name='math')

print(s_name, '\n\n', s_gender, '\n\n', s_math)
print()
[print(name, gender, math) for name, gender, math in zip(s_name, s_gender, s_math)]

df = pd.concat([s_name, s_gender, s_math], axis=1, sort=True)
df = df.set_index([s_name])
print(type(df), '\n', df)

s_stat = pd.Series([76, 73, 95, 10, 25], name='stat', index=['Potter', 'Elsa', 'Gates', 'Wendy', 'Ben'])
df = pd.concat([df, s_stat], axis=1, sort=False)
print(df)

df['score'] = df.math + df.stat
print(df)


def add_grade(x):
    if x >= 150:
        return 'A'
    elif x >= 100:
        return 'B'
    elif x >= 70:
        return 'C'
    else:
        return np.nan


df['grade'] = df.score.apply(lambda x: add_grade(x))
print(df)