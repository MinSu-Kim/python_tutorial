import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyBarChart(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 1200, 600)
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.87, wspace=0.3, hspace=0.2)  # 여백지정
        self.fig = plt.Figure()

        self.canvas = FigureCanvas(self.fig)  # figure - canvas 연동
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

        # 한글 설정
        matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정,
        matplotlib.rcParams['axes.unicode_minus'] = False

        self.fig.suptitle('막대그래프 예제')

        self.do_bar_chart()
        self.do_barh_chart()
        self.do_combo_bar()
        self.built_chart()
        self.canvas.draw()

    def do_bar_chart(self):
        member_IDs = ['m_01', 'm_02', 'm_03', 'm_04']
        before_ex = [27, 35, 40, 33]
        colors = ['r', 'g', 'b', 'm']
        index = np.arange(len(member_IDs))

        ax = self.fig.add_subplot(131)  # fig를 1행 3칸으로 나누어 1칸안에 넣어줍니다
        ax.bar(index, before_ex, tick_label=member_IDs, color=colors, width=0.6)
        ax.set_title('세로 막대 차트')

    def do_barh_chart(self):
        member_IDs = ['m_01', 'm_02', 'm_03', 'm_04']
        before_ex = [27, 35, 40, 33]
        colors = ['r', 'g', 'b', 'm']
        index = np.arange(len(member_IDs))
        ax = self.fig.add_subplot(132)  # fig를 1행 3칸으로 나누어 2칸안에 넣어줍니다
        ax.barh(index, before_ex, tick_label=member_IDs, color=colors)
        ax.set_title('가로 막대 차트')

    def do_combo_bar(self):
        member_IDs = ['m_01', 'm_02', 'm_03', 'm_04']
        before_ex = [27, 35, 40, 33]
        after_ex = [30, 38, 42, 37]
        index = np.arange(len(member_IDs))

        barWidth = 0.4
        ax = self.fig.add_subplot(133)  # fig를 1행 3칸으로 나누어 3칸안에 넣어줍니다

        ax.bar(index, before_ex, color='c', align='edge', width=barWidth, label='before')
        ax.bar(index + barWidth, after_ex, color='m', align='edge', width=barWidth, label='after',
               tick_label=member_IDs)
        ax.legend()
        ax.set_xlabel('회원 ID')
        ax.set_ylabel('윗몸일으키기 횟수')
        ax.set_title('운동 시작 전과 후의 근지구력(복근) 변화 비교')


if __name__ == "__main__":
    app = QApplication([])
    window = MyBarChart()
    window.show()
    app.exec_()
