import pandas as pd
import numpy as np

# 세로 방향 통합
data1 = {'Class1': [95, 92, 98, 100], 'Class2': [91, 93, 97, 99]}
df1 = pd.DataFrame(data1)
print(df1)

data2 = {'Class1': [87, 89],
         'Class2': [85, 90]}
df2 = pd.DataFrame(data2)
print(df2)

df3 = df1.append(df2)
print(df3)

df4 = df1.append(df2, ignore_index=True)
print(df4)

data3 = {'Class1': [96, 83]}
df5 = pd.DataFrame(data3)
print(df5)

df5 = df2.append(df5, ignore_index=True)
print(df5)

# 가로방향 통합
data4 = {'Class3': [93, 91, 95, 98]}
df6 = pd.DataFrame(data4)
print(df6)

df7 = df1.join(df6)
print(df7)

# index라벨을 이용한 가로방향 통합
index_label = ['a', 'b', 'c', 'd']
df1a = pd.DataFrame(data1, index=index_label)
print(df1a)
df4a = pd.DataFrame(data4, index=index_label)
print(df4a)
dfa = df1a.join(df4a)
print(dfa)

data5 = {'Class4': [82, 92]}
df8 = pd.DataFrame(data5)
print(df8)

df9 = df7.join(df8)
print(df9)

# 특정 열을 기준으로 통합하기
table_data1 = {'판매월': ['1월', '2월', '3월', '4월'],
               '제품A': [100, 150, 200, 130],
               '제품B': [90, 110, 140, 170]}
df_a_b = pd.DataFrame(table_data1)
print(df_a_b)

table_data2 = {'판매월': ['1월', '2월', '3월', '4월'],
               '제품C': [112, 141, 203, 134],
               '제품D': [90, 110, 140, 170]}
df_c_d = pd.DataFrame(table_data2)
print(df_c_d)

df_merge = df_a_b.merge(df_c_d)
print(df_merge)