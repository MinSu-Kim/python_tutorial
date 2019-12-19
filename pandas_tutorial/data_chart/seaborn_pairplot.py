import matplotlib.pyplot as plt
import seaborn as sns
 
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

# titanic 데이터셋 중에서 분석 데이터 선택하기
titanic_pair = titanic[['age','pclass', 'fare']]

# 조건에 따라 그리드 나누기
g = sns.pairplot(titanic_pair)
plt.show()

