import pandas as pd
import numpy as np

def stat_ex01():
    table_data3 = {'봄':  [256.5, 264.3, 215.9, 223.2, 312.8],
                   '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
                   '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
                   '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}

    columns_list = ['봄', '여름', '가을', '겨울']
    index_list = ['2012', '2013', '2014', '2015', '2016']

    df = pd.DataFrame(table_data3, index=index_list, columns=columns_list)
    print(df)
    print(df.mean())
    print(df.std())
    print(df.mean(axis=1))#기본값 0:열방향  1:행방향
    print(df.describe())
    print(df.describe())


def stat_ex02():
    KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
                '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
                '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
                '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
                '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
    col_list = ['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX']
    index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

    df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list)
    print(df_KTX)

    print(df_KTX.index)
    print(df_KTX.columns)
    print(df_KTX.values)

    print(df_KTX.head(3))
    print(df_KTX.tail(3))

    print(df_KTX[1:2])
    print(df_KTX.loc['2012'])          # '2012'
    print(df_KTX.loc[index_list[1:2]]) # '2012'

    print(df_KTX['호남선 KTX'])
    print(df_KTX['경부선 KTX']['2012':'2014'])
    print(df_KTX['경부선 KTX'][1:2])
    print(df_KTX[col_list[0:1]])
    print(df_KTX['경부선 KTX'][2:5])

    # 하나의 원소 선택 2016년 호남선 KTX
    print(df_KTX.loc['2016']['호남선 KTX'])
    print(df_KTX.loc['2016','호남선 KTX'])
    print(df_KTX['호남선 KTX']['2016'])
    print(df_KTX['호남선 KTX'][5])
    print(df_KTX['호남선 KTX'].loc['2016'])

    print(df_KTX.T)


if __name__ == '__main__':
    stat_ex01()
    stat_ex02()