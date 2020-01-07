import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 분할
grouped = df.groupby(['class']) 

print("# 그룹별 age 열의 평균 집계 연산")
age_mean = grouped.age.mean()
print(age_mean, '\n')

print("# 그룹별 age 열의 표준편차 집계 연산")
age_std = grouped.age.std()
print(age_std, '\n')

print("# 그룹 객체의 age 열을 iteration으로 z-score를 계산하여 출력")
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]         
    print('* origin :', key)
    print(group_zscore.head(3), '\n')  # 각 그룹의 첫 3개의 행을 출력


# z-score를 계산하는 사용자 함수 정의
def z_score(x): 
    return (x - x.mean()) / x.std()


print("# transform() 메소드를 이용하여 age 열의 데이터를 z-score로 변환")
age_zscore = grouped.age.transform(z_score)  
print(age_zscore.loc[[1, 9, 0]], '\n')     # 1, 2, 3 그룹의 첫 데이터 확인 (변환 결과)
print(len(age_zscore), '\n')              # transform 메소드 반환 값의 길이
print(age_zscore.loc[0:9], '\n')          # transform 메소드 반환 값 출력 (첫 10개)
print(type(age_zscore))             # transform 메소드 반환 객체의 자료형

print("# transform() 메소드를 이용하여 age 열의 데이터를 z-score로 변환")
age_zscore2 = grouped.transform(z_score)
print(age_zscore2.loc[[1, 9, 0]], '\n')     # 1, 2, 3 그룹의 첫 데이터 확인 (변환 결과)
print(len(age_zscore2), '\n')              # transform 메소드 반환 값의 길이
print(age_zscore2.loc[0:9], '\n')          # transform 메소드 반환 값 출력 (첫 10개)
print(type(age_zscore2))             # transform 메소드 반환 객체의 자료형
