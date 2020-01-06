import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def graph_config():
    # 한글 설정
    matplotlib.rcParams['font.family'] = 'NanumGothicCoding'  # '맑은 고딕'으로 설정,
    matplotlib.rcParams['axes.unicode_minus'] = False

    # 그래프 설정
    plt.figure(figsize=(18, 15))
    plt.suptitle("pandas로 그래프 그리기")
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.87, wspace=0.5, hspace=0.2)  # 여백지정


class PandasGraph():
    def __init__(self):
        self._s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self._s2 = pd.Series(np.arange(1, 11), index=pd.date_range('2019-01-01', periods=10))
        self._df_rain = pd.read_csv('../data/sea_rain1.csv', index_col='연도')
        self.prn()

    def prn(self):
        print(self._s1)
        print(self._s2)
        print(self._df_rain)

    def create_line_graph1(self):
        plt.subplot(341)
        self._s1.plot()

    def create_line_graph2(self):
        plt.subplot(342)
        self._s2.plot()

    def create_line_graph3(self):
        plt.subplot(343)
        self._s2.plot(grid=True)

    def create_dataframe_to_line_graph1(self):
        plt.subplot(344)
        plt.plot(self._df_rain)
        plt.xlabel('연도')
        plt.ylabel('강수량')

    def create_dataframe_to_line_graph2(self):
        plt.subplot(345)
        plt.plot(self._df_rain, '>--r')
        plt.xlabel('연도')
        plt.ylabel('강수량')
        plt.title('연간 강수량')
        plt.grid(True)


    def create_dataframe_to_line_graph3(self):
        plt.subplot(236)
        rain_plot = self._df_rain.plot(grid=True, style=['r--*', 'g-o', 'b:*', 'm-.p'])
        rain_plot.set_xlabel("연도")
        rain_plot.set_ylabel("강수량")
        rain_plot.set_title("연간 강수량")
        plt.plot = rain_plot

    def create_dataframe_to_line_graph4(self):
        year = [2006, 2008, 2010, 2012, 2014, 2016]  # 연도
        area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2]  # 1인당 주거면적
        table = {'연도': year, '주거면적': area}
        df_area = pd.DataFrame(table, columns=['연도', '주거면적'])
        df_area.plot(x='연도', y='주거면적', grid=True, title='연도별 1인당 주거면적')

    def create_scatter(self):
        temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
        Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100]
        dict_data = {'기온': temperature, '아이스크림 판매량': Ice_cream_sales}
        df_ice_cream = pd.DataFrame(dict_data, columns=['기온', '아이스크림 판매량'])
        df_ice_cream.plot.scatter(x='기온', y='아이스크림 판매량', grid=True, title='최고 기온과 아이스크림 판매량')

    def create_bar(self):
        grade_num = [5, 14, 12, 3]
        students = ['A', 'B', 'C', 'D']
        df_grade = pd.DataFrame(grade_num, index=students, columns=['Student'])
        grade_bar = df_grade.plot.bar(grid=True)
        grade_bar.set_xlabel("학점")
        grade_bar.set_ylabel("학생수")
        grade_bar.set_title("학점별 학생 수 막대 그래프")

    def create_histo(self):
        math = [76, 82, 84, 83, 90, 86, 85, 92, 72, 71, 100, 87, 81, 76, 94, 78, 81, 60, 79, 69, 74, 87, 82, 68, 79]
        df_math = pd.DataFrame(math, columns=['Student'])
        math_hist = df_math.plot.hist(bins=8, grid=True)
        math_hist.set_xlabel("시험 점수")
        math_hist.set_ylabel("도수(frequency)")
        math_hist.set_title("수학 시험의 히스토그램")

    def create_pie(self):
        fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
        result = [7, 6, 3, 2, 2]
        df_fruit = pd.Series(result, index=fruit, name='선택한 학생수')
        df_fruit.plot.pie()

    def create_pie2(self):
        fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
        result = [7, 6, 3, 2, 2]
        df_fruit = pd.Series(result, index=fruit, name='선택한 학생수')

        explode_value = (0.1, 0, 0, 0, 0)
        fruit_pie = df_fruit.plot.pie(figsize=(5, 5), autopct='%.1f%%', startangle=90, counterclock=False,
                                      explode=explode_value, shadow=False, table=True)
        fruit_pie.set_ylabel("")  # 불필요한 y축 라벨 제거
        fruit_pie.set_title("과일 선호도 조사 결과")
        # 그래프를 이미지 파일로 저장. dpi는 200으로 설정
        plt.savefig('../data/saveFigTest3.png', dpi=200)

    def create_graph(self):
        graph_config()
        self.create_line_graph1()
        self.create_line_graph2()
        self.create_line_graph3()
        self.create_dataframe_to_line_graph1()
        self.create_dataframe_to_line_graph2()
        self.create_dataframe_to_line_graph3()
        # self.create_dataframe_to_line_graph4()
        # self.create_scatter()
        # self.create_bar()
        # self.create_histo()
        # self.create_pie()
        # self.create_pie2()
        plt.show()


if __name__ == "__main__":
    PandasGraph().create_graph()
