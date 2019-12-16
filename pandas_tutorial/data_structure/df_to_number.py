import seaborn as sns

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head(), type(df), sep='\n')  # 첫 5행만 표시
print()

print("# 데이터프레임에 숫자 10 더하기")
addition = df + 10
print(addition.head(), type(addition), sep='\n')  # 첫 5행만 표시
