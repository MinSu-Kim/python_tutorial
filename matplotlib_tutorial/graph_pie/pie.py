import matplotlib.pyplot as plt

from matplotlib_tutorial.graph_bar.bar import graph_config
import matplotlib

class PieDraw():
    def __init__(self):
        self._fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
        self._result = [7, 6, 3, 2, 2]

    def simple_pie(self):
        plt.subplot(221)
        plt.pie(self._result)

    def simple_pie2(self):
        plt.subplot(222)
        plt.pie(self._result, labels=self._fruit, autopct='%.1f%%')

    def simple_pie3(self):
        plt.subplot(223)
        plt.pie(self._result, labels=self._fruit, autopct='%.1f%%', startangle=90, counterclock=False)

    def simple_pie4(self):
        plt.subplot(224)
        explode_value = [0.1, 0, 0, 0, 0]
        plt.pie(self._result, labels=self._fruit, autopct='%.1f%%', startangle=90, counterclock=False, explode=explode_value, shadow=True)

    def create_graph(self):
        # 한글 설정
        matplotlib.rcParams['font.family'] = 'NanumGothicCoding'  # '맑은 고딕'으로 설정,
        matplotlib.rcParams['axes.unicode_minus'] = False
        # 그래프 설정
        figure = plt.figure(figsize=(8, 8))
        figure.suptitle('파이그래프 예제')
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.87, wspace=0.1, hspace=0.1)  # 여백지정

        self.simple_pie()
        self.simple_pie2()
        self.simple_pie3()
        self.simple_pie4()

        plt.savefig('../../data/pie_img_200.png', dpi=200)
        plt.show()


if __name__ == "__main__":
    pieDraw = PieDraw()
    pieDraw.create_graph()