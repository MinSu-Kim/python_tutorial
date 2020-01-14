import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#1. 데이터 로딩
df = pd.read_csv('data/supervised_data.csv', header=0)
#2. 데이터 로딩 확인
print(df)
#3, 그래프로 확인
sns.regplot(x=df.weight, y=df.height, line_kws={'color': 'red'})
plt.show()

res = df.weight.corr(df.height)
print(res)

result = stats.linregress(df.height, df.weight)
print(result)