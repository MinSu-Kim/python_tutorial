from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QWidget, QApplication

from pyqt5_tutorial.layout.boxlayout import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Awesome App')

        layout = QStackedLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))

        layout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()