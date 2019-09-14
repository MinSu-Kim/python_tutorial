import pandas as pd
import numpy as np

def create_series01():
    s = pd.Series([10, 20, 30, 40, 50])
    print(s)

    print(s.index)
    print(s.values)


def create_series02():
    s = pd.Series(['a', 'b', 'c', 1, 2, 3])
    print(s)


def create_series03():
    s = pd.Series([np.nan, 10, 30])
    print(s)


def input_series():
    index_data = ['2019-09-13', '2019-09-14', '2019-09-15', '2019-09-16']
    s = pd.Series([200, 195, np.nan, 205], index=index_data)
    print(s)

    s1 = pd.Series({'국어': 100, '영어': 90, '수학': 80}) #dictionary 사용 {key:value}
    print(s1)


def date_auto_create():
    s = pd.date_range(start='2019-09-11', end='2019-09-14')
    print(s)
    s = pd.date_range(start='2019-09-11', periods=7)
    print(s)


if __name__ == '__main__':
    create_series01()
    create_series02()
    create_series03()
    input_series()
    date_auto_create()