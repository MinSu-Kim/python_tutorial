import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp


class MyApp(QMainWindow):

    def __init__(self):     # self는 MyApp 객체
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')    # 타이틀바에 나타나는 창의 제목을 설정
        self.setGeometry(300, 300, 400, 200)

        exitAction = QAction(QIcon('icon/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)        #  macOS에서도 Windows 환경과 동일한 결과를 보여주기 위함
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()