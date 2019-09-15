import matplotlib.pyplot as plt
import numpy as np


class LineDecorate():
    def __init__(self):
        self.x = np.arange(0, 5, 1)
        self.y1 = self.x
        self.y2 = self.x + 1
        self.y3 = self.x + 2
        self.y4 = self.x + 3

    def __draw_line(self):
        plt.subplot(2, 3, 1)
        plt.plot(self.x, self.y1)
        plt.plot(self.x, self.y2)
        plt.plot(self.x, self.y3)
        plt.plot(self.x, self.y4)

    def __draw_line_color(self):
        plt.subplot(2, 3, 2)
        plt.plot(self.x, self.y1, 'm')  # m 자홍색(magenta)
        plt.plot(self.x, self.y2, 'y')  # y 노란색(yellow)
        plt.plot(self.x, self.y3, 'k')  # k 검은색(black)
        plt.plot(self.x, self.y4, 'c')  # c 청녹생(cyan)

    def __draw_line_lineStyle(self):
        plt.subplot(2, 3, 3)
        plt.plot(self.x, self.y1, '-')   # -  실선(solid line)
        plt.plot(self.x, self.y2, '--')  # -- 파선(dashed line)
        plt.plot(self.x, self.y3, ':')   # :  점선(dotted line)
        plt.plot(self.x, self.y4, '-.')  # -. 파선 점선 혼합(dash-dot line)

    def __draw_line_maker(self):
        plt.subplot(2, 3, 4)
        plt.plot(self.x, self.y1, 'o')   # 원모양
        plt.plot(self.x, self.y2, '^')   # 위쪽 삼각형
        plt.plot(self.x, self.y3, 's')   # 사각형(square)
        plt.plot(self.x, self.y4, 'd')   # 다이아몬드(diamond)

    def __draw_mix(self):
        plt.subplot(2, 3, 5)
        plt.plot(self.x, self.y1, '>--r')
        plt.plot(self.x, self.y2, 's-g')
        plt.plot(self.x, self.y3, 'd:b')
        plt.plot(self.x, self.y4, '-.Xc')

    def draw(self):
        self.__draw_line()
        self.__draw_line_color()
        self.__draw_line_lineStyle()
        self.__draw_line_maker()
        self.__draw_mix()
        plt.show()