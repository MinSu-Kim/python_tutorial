import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# 한글 설정
import platform
print(platform.system())

if platform.system() == 'Windows':
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정
else:
    matplotlib.rcParams['font.family'] = 'NanumGothicCoding'  # '맑은 고딕'으로 설정,

matplotlib.rcParams['axes.unicode_minus'] = False

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 20)  # 출력할 최대 열의 개수
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비

# 파일 불러오기
df_2015_2019 = pd.read_csv('전국 전체 분양가격(2015_2019).csv', encoding='utf-8')
print(df_2015_2019.shape, '\n', df_2015_2019.head(), '\n', df_2015_2019.tail())

df_2013_2015 = pd.read_csv('전국 평균 분양가격(2015년 09월까지).csv',
                           encoding='euc-kr',
                           skiprows=1,
                           header=0, engine='python')

print(df_2013_2015.shape, '\n', df_2013_2015.head(), '\n', df_2013_2015.tail())

print(df_2013_2015.columns)

# 24열 이후 삭제(통계정보)
df_2013_2015 = df_2013_2015.drop(columns=df_2013_2015.columns[24:])
print(df_2013_2015.columns)

year = df_2013_2015.iloc[0]
# 결측치를 전의 값으로 채워줌
year = year.fillna(method='ffill')
year

month = df_2013_2015.iloc[1]
print(year, '\n', month)

for i, y in enumerate(year):
    if i > 1:
        year[i] = ' '.join([str(year[i]), '{:,.0f}'.format(month[i])])
year[1] = '시군구'

print(year)

df_2013_2015.columns = year
print(df_2013_2015)

# 통계정보 제거
df_2013_2015 = df_2013_2015.drop(df_2013_2015.index[[0, 1, 2, 10, 12, 22]])
print(df_2013_2015)

df_2013_2015.loc[4, '구분'] = ''
df_2013_2015.loc[14, '구분'] = ''
print(df_2013_2015)

# 지역 컬럼을 새로 만들어 시도와 시군구를 병합
# 결측치 빈문자로
df_2013_2015['구분'] = df_2013_2015['구분'].fillna('')
df_2013_2015.시군구 = df_2013_2015.시군구.fillna('')
print(df_2013_2015)
df_2013_2015['지역명'] = df_2013_2015.구분 + df_2013_2015.시군구
#
print(df_2013_2015)

print(df_2013_2015.drop(['구분', '시군구'], axis=1))
df_2013_2015 = df_2013_2015.drop(['구분', '시군구'], axis=1)


# 여기까지
print("df_2013_2015", '\n', df_2013_2015, '\n')
melt_columns = df_2013_2015.columns.copy()
print(melt_columns, type(melt_columns))


# df_2013_2015 = pd.melt(df_2013_2015, id_vars=['지역명'],
#                        value_vars=['2013 12', '2014 1', '2014 2', '2014 3', '2014 4',
#                                    '2014 5', '2014 6', '2014 7', '2014 8', '2014 9', '2014 10', '2014 11',
#                                    '2014 12', '2015 1', '2015 2', '2015 3', '2015 4', '2015 5', '2015 6',
#                                    '2015 7', '2015 8', '2015 9'])

# index를 list로 변경
melt_columns = melt_columns[:len(melt_columns)-1].tolist()
print("melt_columns", '\n', melt_columns)


df_2013_2015 = pd.melt(df_2013_2015, id_vars=['지역명'],
                       value_vars=melt_columns)

print(df_2013_2015.head())

# 지역명, 0, value => '지역명', '기간', '분양가'로 열이름 변경
df_2013_2015.columns = ['지역명', '기간', '분양가']
print(df_2013_2015.head())

# 기간을 연도와 월로 분리하여  추가
df_2013_2015['연도'] = df_2013_2015['기간'].apply(lambda year_month: year_month.split(' ')[0])
df_2013_2015['월'] = df_2013_2015['기간'].apply(lambda year_month: year_month.split(' ')[1])

print(df_2013_2015.head())
print(df_2015_2019.head())

print(df_2015_2019.info(), '\n\n')

print(df_2013_2015.info(), '\n\n')
df_2013_2015.연도 = df_2013_2015.연도.astype(int)
df_2013_2015.월 = df_2013_2015.월.astype(int)
print(df_2013_2015.info(), '\n\n')

plt.figure(figsize=(18, 10))
plt.subplot(221)
sns.boxplot(data=df_2013_2015, x='지역명', y='분양가', hue='연도')

plt.subplot(222)
sns.barplot(data=df_2013_2015, x='지역명', y='분양가', hue='연도')

plt.subplot(223)
sns.boxplot(data=df_2015_2019, x='지역명', y='평당분양가격', hue='연도')

plt.subplot(224)
sns.barplot(data=df_2015_2019, x='지역명', y='평당분양가격', hue='연도')
plt.suptitle("2013-2015, 2015-2019년 지역별 평당분양가격", size=20)
plt.show()


# 컬럼명 맞추기
print(df_2013_2015.columns, '\n\n', df_2015_2019.columns, '\n\n')

df_2013_2015_prepare = df_2013_2015[['지역명', '연도', '월', '분양가']]
total_columns = ['지역명', '연도', '월', '평당분양가격']
df_2013_2015_prepare.columns = total_columns

df_2015_2019_prepare = df_2015_2019[['지역명', '연도', '월', '평당분양가격']]

print(df_2013_2015_prepare.head(), '\n\n', df_2015_2019_prepare.head())
print(df_2013_2015_prepare.shape, '\n\n', df_2015_2019_prepare.shape)

# 결합하기
df_2013_2019 = pd.concat([df_2013_2015_prepare, df_2015_2019_prepare])
print("total : ", df_2013_2019.shape)

# 2013년부터 2019년 11월 전국 신규 민간 아파트 분양가격 동향 시각화
df_year_mean = df_2013_2019.groupby(['연도'])['평당분양가격'].mean()
print(df_year_mean)

fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.87, wspace=0.5, hspace=0.5)  # 여백지정

df_year_mean.plot.bar(rot=0, ax=ax1)
sns.barplot(data=df_2013_2019, x='연도', y='평당분양가격', ax=ax2)
df_2013_2019[['연도', '지역명', '평당분양가격']].boxplot(by=['연도'], ax=ax3)
df_2013_2019_daegu = df_2013_2019.loc[df_2013_2019.지역명 == '대구']
sns.boxplot(x='연도', y='평당분양가격', data=df_2013_2019_daegu, ax=ax4)

ax1.set_title('연도별 평균 평당분양가격 - bar')
ax2.set_title('연도별 평균 평당분양가격 - seaborn')
ax3.set_title('연도별 평균 평당분양가격 - boxplot')
ax4.set_title('대구 연도별 평균 평당분양가격 - boxplot')
fig.suptitle('연도별 평균 평당분양가격')
plt.show()
