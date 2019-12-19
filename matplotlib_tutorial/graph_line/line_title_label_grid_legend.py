import matplotlib
import matplotlib.font_manager
import matplotlib.pyplot as plt
import numpy as np


class LineDetail():

    def __init__(self):
        self.x = np.arange(-4.5, 5, 0.5)
        self.y = 2 * self.x ** 3

        self.x1 = np.arange(0, 5, 1)
        self.y1 = self.x1
        self.y2 = self.x1 + 1
        self.y3 = self.x1 + 2
        self.y4 = self.x1 + 3

        self.column = 3
        self.row = 2

        figure = plt.figure(figsize=(14, 8))
        figure.suptitle('Graph Detail')
        # plt.rcParams["figure.figsize"] = (15, 8)
        # plt.rcParams['lines.linewidth'] = 4
        # plt.rcParams['lines.color'] = 'r'
        # plt.rcParams['axes.grid'] = True

    def __draw_line_Label(self):
        # plt.subplot(self.row, self.column, 1)
        plt.subplot(231)  # 행열번호
        plt.plot(self.x, self.y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

    def __draw_line_Title(self):
        plt.title("Graph title")

    def __draw_line_Grid(self):
        plt.grid(True)

    def __draw_line_Legend(self):
        plt.subplot(self.row, self.column, 2)
        plt.plot(self.x1, self.y1, '>--r', self.x1, self.y2, 's-g', self.x1, self.y3, 'd:b', self.x1, self.y4, '-.Xc')
        plt.legend(['data1', 'data2', 'data3', 'data4'])

    def __draw_line_Lenend_which(self):
        plt.subplot(self.row, self.column, 3)
        plt.plot(self.x1, self.y1, '>--r', self.x1, self.y2, 's-g', self.x1, self.y3, 'd:b', self.x1, self.y4, '-.Xc')
        plt.legend(['data1', 'data2', 'data3', 'data4'], loc='lower right')

    def __draw_line_full(self):
        plt.subplot(self.row, self.column, 4)
        plt.plot(self.x1, self.y1, '>--r', self.x1, self.y2, 's-g', self.x1, self.y3, 'd:b', self.x1, self.y4, '-.Xc')
        plt.legend(['data1', 'data2', 'data3', 'data4'], loc='lower right')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Graph Title')
        plt.grid()

    def __draw_line_han(self):
        # 기본폰트 확인 ['sans-serif']
        print('matplotlib.rcParams[\'font.family\']\n', matplotlib.rcParams['font.family'])
        # 사용가능한 폰트 확인
        matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정,
        matplotlib.rcParams['axes.unicode_minus'] = False

        plt.subplot(self.row, self.column, 5)
        plt.plot(self.x1, self.y1, '>--r', self.x1, self.y2, 's-g', self.x1, self.y3, 'd:b', self.x1, self.y4, '-.Xc')
        plt.legend(['데이터1', '데이터2', '데이터3', '데이터4'], loc='best')
        plt.xlabel('X 축')
        plt.ylabel('Y 축')
        plt.title('그래프 제목')
        plt.grid()

    def __draw_line_str(self):
        plt.subplot(self.row, self.column, 6)
        plt.plot(self.x1, self.y1, '>--r', self.x1, self.y2, 's-g', self.x1, self.y3, 'd:b', self.x1, self.y4, '-.Xc')
        plt.text(0, 6, '문자열 출력 1')
        plt.text(0, 5, '문자열 출력 2')
        plt.text(3, 1, '문자열 출력 3')
        plt.text(3, 0, '문자열 출력 4')

    def draw_line(self):
        # 상하좌우 값들은 Figure객체 안에서 여백의 크기를, Figure크기에 대한 비율.
        # Width Space와 Height Space 값은 Axes객체 하나 크기의 비율.
        plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.87, wspace=0.25, hspace=0.3)  # 여백지정
        self.__draw_line_Label()
        self.__draw_line_Title()
        self.__draw_line_Grid()
        self.__draw_line_Legend()
        self.__draw_line_Lenend_which()
        self.__draw_line_full()
        self.__draw_line_han()
        self.__draw_line_str()

        plt.show()
