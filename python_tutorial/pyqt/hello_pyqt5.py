import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("HelloPyQt5.ui")
        self.ui.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyApp()
    sys.exit(app.exec())