import matplotlib.pyplot as plt
import numpy as np


class LinePlot():

    def __init__(self):
        self.data1 = [10, 14, 19, 20, 25]
        self.x = np.arange(-4.5, 5, 0.5)
        self.y = 2*self.x**2

    def graph_line(self):
        plt.plot(self.data1)
        plt.show()

    def multi_line01(self):
        plt.plot(self.data1)
        plt.plot(self.x, self.y)
        plt.show()

    def multi_line02(self):
        plt.plot(self.data1)
        plt.figure()
        plt.plot(self.x, self.y)
        plt.show()

    def multi_line03(self):
        x = np.arange(-4.5, 5, 0.5)
        y1 = 2*x**2
        y2 = 5*x + 30
        y3 = 4 * x ** 2 + 10
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.plot(x, y3)
        plt.figure()
        plt.plot(x, y1, x, y2, x, y3)
        plt.show()

    @staticmethod
    def multi_line04():
        # 데이터 생성",
        x = np.arange(-5, 5, 0.1)
        y1 = x**2 - 2
        y2 = 20*np.cos(x) ** 2  # NumPy에서 cos()는 np.cos()으로 입력

        plt.figure(1)    # 1번 그래프 창을 생성함
        plt.plot(x, y1)  # 지정된 그래프 창에 그래프를 그림
        plt.figure(2)    # 2번 그래프 창을 생성함
        plt.plot(x, y2)  # 지정된 그래프 창에 그래프를 그림

        plt.figure(1)    # 이미 생성된 1번 그래프 창을 지정함
        plt.plot(x, y2)  # 지정된 그래프 창에 그래프를 그림

        plt.figure(2)    # 이미 생성된 2번 그래프 창을 지정함
        plt.clf()        # 2번 그래프 창에 그려진 모든 그래프를 지움
        plt.plot(x, y1)  # 지정된 그래프 창에 그래프를 그림

        plt.show()