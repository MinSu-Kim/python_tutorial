import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 설정
matplotlib.rcParams['font.family'] = 'NanumGothicCoding'  # '맑은 고딕'으로 설정,

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 20)  # 출력할 최대 열의 개수
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비
matplotlib.rcParams['axes.unicode_minus'] = False

# 파일 불러오기
pre_sale = pd.read_csv('전국 평균 분양가격(2015년 10월부터 2019년 11월).csv', encoding='euc-kr')
print(pre_sale.shape, '\n')
print(pre_sale.head(), '\n')
print(pre_sale.tail(), '\n')

print("# 분양가격이 숫자 타입이 아님, 숫자 타입으로 변경")
print(pre_sale.info(), '\n')
print(pre_sale.dtypes, '\n')

print("# 결측치 확인")
print(pre_sale.isnull().sum(), '\n')

print("pre_sale['분양가격(㎡)'].value_counts(dropna=False)")
print(pre_sale['분양가격(㎡)'].value_counts(dropna=False), '\n')


print("# 연도와 월은 카테고리 형태의 데이터이기 때문에 스트링 형태로 변경")
pre_sale['연도'] = pre_sale['연도'].astype(str)
pre_sale['월'] = pre_sale['월'].astype(str)
print(pre_sale.dtypes, '\n')

print("# 분양가격의 타입을 숫자로 변경")
pre_sale_price = pre_sale['분양가격(㎡)']
# If 'coerce', then invalid parsing will be set as NaN
pre_sale['분양가격'] = pd.to_numeric(pre_sale_price, errors='coerce')
pre_sale = pre_sale.drop(['분양가격(㎡)'], axis=1)
print(pre_sale.head(), '\n')

print("# 평당 분양가격 계산")
pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3
print(pre_sale.head(), '\n')



# [print(pre_sale[x].value_counts(dropna=False), '\n') for x in pre_sale.columns]
# print(pre_sale['분양가격(㎡)'].value_counts(dropna=False), '\n')

print("# 수치형 자료만 요약하여 보기")
print(pre_sale.describe(), '\n')

print("# 문자열 요약하여 보기")
print(pre_sale.describe(include=[np.object]), '\n')

print("# 2017년 데이터보기")
pre_sale_2017 = pre_sale.loc[pre_sale['연도'] == '2017']
print(pre_sale_2017.shape, '\n')

print("pre_sale['규모구분'].value_counts()")
print(pre_sale['규모구분'].value_counts(), '\n')

print("pre_sale['지역명'].value_counts()")
print(pre_sale['지역명'].value_counts(), '\n')


# 전국평균 분양가격 groupby와 pivot_table활용하기
# 분양가격만 봤을 때 2015년에서 2019년으로 갈수록 오른 것을 확인
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 20)  # 출력할 최대 열의 개수
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비
matplotlib.rcParams['axes.unicode_minus'] = False

pd.options.display.float_format = '{:,.0f}'.format
print(pre_sale.groupby(pre_sale.연도).describe(), '\n')

print(pre_sale.pivot_table(values='평당분양가격', index='규모구분', columns='연도'), '\n')


print("# 규모구분에서 전체로 되어 있는 데이터만 가져오기")
region_year_all = pre_sale.loc[pre_sale['규모구분'] == '전체']
print(region_year_all, '\n')

print(region_year_all.pivot_table(values='평당분양가격', index='지역명', columns='연도'), '\n')

print("# reset_index")
region_year = region_year_all.pivot_table('평당분양가격', '지역명', '연도').reset_index()
print(region_year, '\n')


# 2015년에서 2019년 변동액 계산
region_year['변동액'] = (region_year['2019'] - region_year['2015']).astype(float)
print(region_year)
print(region_year.sort_values('변동액', ascending=False))
region_year_sort = region_year.sort_values('변동액', ascending=False)

max_delta_price = np.max(region_year['변동액']) * 1000
min_delta_price = np.min(region_year['변동액']) * 1000
mean_delta_price = np.mean(region_year['변동액']) * 1000

print('2015년 부터 2019년까지 분양가는 계속 상승했으며, 상승액이 가장 큰 지역은 서울이며 상승액은 평당{:,.0f}원이다.'
      .format(max_delta_price))
print('상승액이 가장 작은 지역은 울산이며 평당 {:,.0f}원이다.'.format(min_delta_price))
print('하지만 나중에 살펴보겠지만 울산에는 결측치가 많다. 따라서 변동액이 가장 작다고 판단하기 어렵다.')
print('전국 평균 변동액은 평당 {:,.0f}원이다.'.format(mean_delta_price))

sns.set_style('whitegrid')

# window의 한글폰트 설정
plt.rc('font', family='NanumGothicCoding')
# Mac 한글폰트
# plt.rc('font', family='AppleGothic')

plt.figure(figsize=(20, 8))
plt.title('2015-2019년 신규 민간 아파트 분양가격')

sns.barplot(data=region_year_all, x='지역명', y='평당분양가격', hue='연도')
plt.show()

df_year_region = pd.pivot_table(region_year_all,
                                index=['지역명'],
                                columns='연도',
                                values='평당분양가격')

print(df_year_region.sample(3))

df_year_region.plot.bar(figsize=(24, 8), grid=True, fontsize=20, rot=0,
                        title='지역, 연도별 평당 평균 분양가')
plt.show()

# 지역별 평당 분양가격 합계
print(pre_sale.pivot_table('평당분양가격', '규모구분', '지역명'))

# 서울의 경우 전용면적 85㎡초과 102㎡이하가 분양가격이 가장 비싸게 나옵니다.
plt.figure(figsize=(20, 8))
sns.barplot(data=pre_sale, x='지역명', y='평당분양가격', hue='규모구분')
plt.show()

# 지역별 평당 분양가격 합계
pre_sale_size = pre_sale.pivot_table(values='평당분양가격', index='지역명', columns='규모구분')
print(pre_sale_size.sample(3))

pre_sale_size.plot.bar(title='지역, 규모구분 별 평당 평균 분양가',
                       figsize=(20, 8),
                       grid=True,
                       fontsize=20,
                       rot=0);
plt.show()

# 규모구분 == '전용면적 102㎡초과' nan 확인
print(pre_sale[(pre_sale.지역명 == '대전') & (pre_sale.규모구분 == '전용면적 102㎡초과')])

pre_sale_size_t = pre_sale_size.T
print(pre_sale_size_t)

# 결측치 확인
print(pre_sale.평당분양가격.isnull().sum())

# 결측치가 있으면 제대로 된 시각화를 할 수 없기 때문에 drop
print(pre_sale.평당분양가격.dropna(inplace=True, axis=0))

# 결측치 확인
print(pre_sale.평당분양가격.isnull().sum())

print(pre_sale.dtypes)

# 아래 그래프를 통해 지역마다 0 값이 존재하는 것으로 결측치가 있음을 확인
pre_sale[['지역명', '평당분양가격']].boxplot(by=['지역명'], figsize=(18, 6))
plt.show()

pre_sale[['연도', '지역명', '평당분양가격']].boxplot(
    by=['지역명', '연도'],
    figsize=(18, 6),
    fontsize=12,
    rot=60
)
plt.show()

pre_sale_seoul = pre_sale[pre_sale['지역명'] == '서울']
print(pre_sale_seoul)

# 2013년 12월이후 2015년 9월 까지의 데이터와 병합하기 위해 파일로 저장
df_2015_2019 = pre_sale.loc[pre_sale['규모구분'] == '전체']
df_2015_2019.to_csv('전국 전체 분양가격(2015_2019).csv')