import seaborn as sns

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())
print()


# 사용자 함수 정의
def add_two_obj(a, b):  # 두 객체의 합
    return a + b


print("# 데이터프레임의 2개 열을 선택하여 적용")
print("# x=df, a=df['age'], b=df['ten']")
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)
print(df.head())
