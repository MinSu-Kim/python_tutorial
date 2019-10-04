import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("HelloPyQt5.ui")
        self.ui.pushButton.clicked.connect(self.btn_clicked)
        self.ui.show()

    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyApp()
    sys.exit(app.exec())
