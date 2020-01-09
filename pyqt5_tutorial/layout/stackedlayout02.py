from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QStackedLayout, QPushButton, QWidget, QApplication

from pyqt5_tutorial.layout.boxlayout import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(layout)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow']):
            btn = QPushButton(color)
            btn.pressed.connect( lambda n=n: layout.setCurrentIndex(n))
            button_layout.addWidget(btn)
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()