import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def graph_config(title, width=12):
    # 한글 설정
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정,
    matplotlib.rcParams['axes.unicode_minus'] = False
    # 그래프 설정
    figure = plt.figure(figsize=(width, 5))
    figure.suptitle(title)
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.87, wspace=0.1, hspace=0.1)  # 여백지정


class BarDraw():
    def __init__(self):
        self._member_IDs = ['m_01', 'm_02', 'm_03', 'm_04']
        self._before_ex = [27, 35, 40, 33]
        self._after_ex = [30, 38, 42, 37]
        self._index = np.arange(len(self._member_IDs))

    def create_bar(self):
        plt.subplot(131)
        colors = ['r', 'g', 'b', 'm']
        plt.bar(self._index, self._before_ex, tick_label = self._member_IDs, color=colors, width=0.6)
        plt.title('세로 막대 차트')

    def create_barh(self):
        plt.subplot(132)
        index = np.arange(len(self._member_IDs))
        colors = ['r', 'g', 'b', 'm']
        plt.barh(index, self._before_ex, color=colors, tick_label=self._member_IDs)
        plt.title('가로 막대 차트')

    def create_combo_bar(self):
        plt.subplot(133)
        barWidth = 0.4
        plt.bar(self._index, self._before_ex, color='c', align='edge', width=barWidth, label='before')
        plt.bar(self._index + barWidth, self._after_ex, color='m', align='edge', width=barWidth, label='after')
        plt.xticks(self._index + barWidth, self._member_IDs)
        plt.legend()
        plt.xlabel('회원 ID')
        plt.ylabel('윗몸일으키기 횟수')
        plt.title('운동 시작 전과 후의 근지구력(복근) 변화 비교')

    def create_graph(self):
        graph_config('막대그래프 예제')
        self.create_bar()
        self.create_barh()
        self.create_combo_bar()
        plt.show()


if __name__ == "__main__":
    barDraw = BarDraw()
    barDraw.create_graph()