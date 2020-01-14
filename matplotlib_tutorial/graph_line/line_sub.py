import matplotlib.pyplot as plt
import numpy as np


class SubLine():
    def __init__(self):
        # 데이터 생성\n",
        self.x = np.arange(0, 10, 0.1)
        self.y1 = 0.3 * (self.x - 5) ** 2 + 1
        self.y2 = -1.5 * self.x + 3
        self.y3 = np.sin(self.x) ** 2  # NumPy에서 sin()은 np.sin()으로 입력
        self.y4 = 10 * np.exp(-self.x) + 1  # NumPy에서 exp()는 np.exp()로 입력

        self.x1 = np.linspace(-4, 4, 100)   # [-4, 4] 범위에서 100개의 값 생성
        self.y11 = self.x1 ** 3
        self.y12 = 10 * self.x1 ** 2 -2

    def draw_subline(self):
        # 2 × 2 행렬로 이뤄진 하위 그래프에서 p에 따라 위치를 지정
        plt.subplot(2, 2, 1)        # p는 1
        plt.plot(self.x, self.y1)

        plt.subplot(2, 2, 2)        # p는 2
        plt.plot(self.x, self.y2)

        plt.subplot(2, 2, 3)        # p는 3
        plt.plot(self.x, self.y3)

        plt.subplot(2, 2, 4)        # p는 4
        plt.plot(self.x, self.y4)

        plt.show()

    def draw_line_lim(self):
        plt.subplot(2, 1, 1)
        plt.plot(self.x1, self.y11, self.x1, self.y12)

        plt.subplot(2, 1, 2)
        plt.plot(self.x1, self.y11, self.x1, self.y12)
        plt.xlim(-1, 1)
        plt.ylim(-3, 3)

        plt.show()
