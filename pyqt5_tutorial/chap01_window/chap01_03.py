import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Firsrt App")

        label = QLabel('This is a PyQt5 window!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()