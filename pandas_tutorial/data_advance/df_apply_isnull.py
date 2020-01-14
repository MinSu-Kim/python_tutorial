import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print()


# 사용자 함수 정의
def missing_value(series):  # 시리즈를 인수로 전달
    return series.isnull()  # 불린 시리즈를 반환


print("# 데이터프레임의 각 열을 인수로 전달하면 데이터프레임을 반환")
result = df.apply(missing_value, axis=0)
print(result.head(), type(result), sep='\n')
