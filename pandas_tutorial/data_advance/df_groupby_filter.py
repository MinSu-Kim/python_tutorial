import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 분할
grouped = df.groupby(['class']) 

print("# 그룹 객체를 iteration으로 출력: head() 메소드로 첫 5행만을 출력")
for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print("age(mean) :", group.age.mean())
    print()

print("# 데이터 개수가 200개 이상인 그룹만을 필터링하여 데이터프레임으로 반환")
grouped_filter = grouped.filter(lambda x: len(x) >= 200)  
print(grouped_filter.head(), '\n', type(grouped_filter), '\n')

print(grouped_filter['class'].value_counts())
print()

print("# age 열의 평균이 30보다 작은 그룹만을 필터링하여 데이터프레임으로 반환")
print(grouped['class'].value_counts(),'\n')
age_filter = grouped.filter(lambda x: x.age.mean() < 30)  
print(age_filter.tail(), '\n\n', type(age_filter), '\n\n', age_filter['class'].value_counts())
