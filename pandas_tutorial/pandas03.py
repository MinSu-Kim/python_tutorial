import pandas as pd
import numpy as np


def df_operator01():
    df1 = pd.Series(np.arange(1, 6))
    print(df1)
    df2 = pd.Series(np.arange(10, 60, 10))
    print(df2)

    print(df1 + df2)
    print(df2 - df1)
    print(df1 * df2)
    print(df2 / df1)

    df3 = pd.Series(np.arange(10, 80, 10))
    print(df2 + df3)


def df_operator02():
    table_data01 = {'A': [1, 2, 3, 4, 5],
                    'B': [10, 20, 30, 40, 50],
                    'C': [100, 200, 300, 400, 500]}
    df1 = pd.DataFrame(table_data01)
    print(df1)

    table_data02 = {'A': [6, 7, 8],
                    'B': [60, 70, 80],
                    'C': [600, 700, 800]}
    df2 = pd.DataFrame(table_data02)
    print(df2)

    print(df1 + df2)


if __name__ == '__main__':
    df_operator01()
    df_operator02()
