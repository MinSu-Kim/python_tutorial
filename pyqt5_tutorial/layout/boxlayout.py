import sys

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        vLayout = QVBoxLayout()
        vLayout.addWidget(Color('red'))
        vLayout.addWidget(Color('green'))
        vLayout.addWidget(Color('blue'))

        hLayout = QHBoxLayout()
        hLayout.addWidget(Color('red'))
        hLayout.addWidget(Color('green'))
        hLayout.addWidget(Color('blue'))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 안쪽여백
        layout.setSpacing(5)                   # 위젯간의 간격

        layout.addLayout(vLayout)
        layout.addLayout(hLayout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()