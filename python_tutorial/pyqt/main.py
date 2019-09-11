import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from python_tutorial.pyqt import HelloPyQt5

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = HelloPyQt5.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
