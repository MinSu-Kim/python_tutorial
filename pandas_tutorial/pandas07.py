import pandas as pd


class ReadWrite():
    def __init__(self):
        self.readData = pd.read_csv('../data/sea_rain1.csv')
        self.readData_ms949 = pd.read_csv('../data/sea_rain1_from_notepad.csv', encoding='cp949')
        self.readData_space = pd.read_csv('../data/sea_rain1_space.csv', sep=' ')
        self.readData_index_col = pd.read_csv('../data/sea_rain1.csv', index_col='연도')
        self.df_WH = pd.DataFrame({'Weight': [62, 67, 55, 74],
                                   'Height': [165, 177, 160, 180]},
                                  index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])
        self.df_WH.index.name = 'User'

    def prn(self):
        print(self.readData)
        print(self.readData_ms949)
        print(self.readData_space)
        print(self.readData_index_col)
        print(self.df_WH)

    def create_dataFrame_to_csv(self):
        self.df_WH['BMI'] = self.df_WH['Weight']/(self.df_WH['Height']/100)**2
        print(self.df_WH)
        self.df_WH.to_csv('../data/save_dataframe.csv')

        df_pr = pd.DataFrame({'판매가격': [2000, 3000, 5000, 10000],
                              '판매량': [32, 53, 40, 25]},
                             index=['P1001', 'P1002', 'P1003', 'P1004'])
        df_pr.index.name = '제품번호'
        print(df_pr)
        file_name = '../data/save_dataframe_cp949.txt'
        df_pr.to_csv(file_name, sep=' ', encoding='cp949')


if __name__ == '__main__':
    rw = ReadWrite()
    rw.prn()
    rw.create_dataFrame_to_csv()
    print(pd.read_csv('../data/save_dataframe.csv'))
    print(pd.read_csv('../data/save_dataframe_cp949.txt', encoding='cp949'))