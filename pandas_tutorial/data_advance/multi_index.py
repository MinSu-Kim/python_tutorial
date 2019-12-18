import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열, sex 열을 기준으로 분할
grouped = df.groupby(['class', 'sex'])  

print("# 그룹 객체에 연산 메서드 적용")
gdf = grouped.mean()
print(gdf, '\n', type(gdf))

print("# class 값이 First인 행을 선택하여 출력")
print(gdf.loc['First'], '\n')

print("# class 값이 First이고, sex 값이 female인 행을 선택하여 출력")
print(gdf.loc[('First', 'female')], '\n')

print("# sex 값이 male인 행을 선택하여 출력")
print(gdf.xs('male', level='sex'))
