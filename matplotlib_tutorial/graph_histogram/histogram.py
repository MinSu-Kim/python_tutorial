import matplotlib.pyplot as plt
from matplotlib_tutorial.graph_bar.bar import graph_config


class HistoDraw():
    def __init__(self):
        self._math = [76, 82, 84, 83, 90, 86, 85, 92, 72, 71, 100, 87, 81, 76, 94, 78, 81, 60, 79, 69, 74, 87, 82, 68, 79]
        graph_config('히스토그램 예제', 18)

    def simple_histo1(self):
        plt.subplot(131)
        plt.hist(self._math)

    def simple_histo2(self):
        plt.subplot(132)
        plt.hist(self._math, bins=8)

    def simple_histo3(self):
        plt.subplot(133)
        plt.hist(self._math, bins=8)
        plt.xlabel('시험 점수')
        plt.ylabel('도수(frequency')
        plt.title('수학 시험의 히스토그램')
        plt.grid()

    def create_graph(self):
        self.simple_histo1()
        self.simple_histo2()
        self.simple_histo3()
        plt.show()


if __name__ == "__main__":
    histoDraw = HistoDraw()
    histoDraw.create_graph()
