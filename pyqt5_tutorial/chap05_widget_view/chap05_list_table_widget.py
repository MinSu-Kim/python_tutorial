from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QHBoxLayout, QListWidget, QMainWindow, QApplication, \
    QWidget, QLineEdit, QPushButton, QSpinBox

from pyqt5_tutorial.chap05_widget_view.chap05_list import MySimpleList


class MyListTable(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget & QTableWidget')
        self.setGeometry(0, 0, 600, 400)
        self.init_ui()

    def init_ui(self):
        group_list = MySimpleList()

        layout = QVBoxLayout()
        layout.addWidget(group_list)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    win = MyListTable()
    win.show()
    app.exec_()