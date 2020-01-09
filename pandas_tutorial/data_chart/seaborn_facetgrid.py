import matplotlib.pyplot as plt
import seaborn as sns
 
titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

# 조건에 따라 그리드 나누기
g = sns.FacetGrid(data=titanic, col='who', row='survived') 

# 그래프 적용하기
g = g.map(plt.hist, 'age')
plt.show()
