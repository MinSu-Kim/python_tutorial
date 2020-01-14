import pandas as pd
import numpy as np


def dataframe_ex01():
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(df)

    data_list = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    df2 = pd.DataFrame(data_list)
    print(df2)

    index_date = pd.date_range('2019-09-11', periods=3)
    column_list=['A', 'B', 'C']
    df3=pd.DataFrame(data_list, index=index_date, columns=column_list)
    print(df3)

    #dictionary
    table_data = {'연도': [2015, 2016, 2016, 2017, 2017],
                  '지사': ['한국', '한국', '미국', '한국', '미국'],
                  '고객수': [200, 250, 450, 300, 500]}
    print(table_data)
    df4= pd.DataFrame(table_data)
    print(df4)

    df5 = pd.DataFrame(table_data, columns=['연도', '고객수', '지사'])
    print(df5)
    print(df5.index)
    print(df5.columns)
    print(df5.values)


if __name__ == '__main__':
    dataframe_ex01()