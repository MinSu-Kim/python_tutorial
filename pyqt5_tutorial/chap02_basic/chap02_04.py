from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolTip, QGroupBox, QVBoxLayout, \
    QStatusBar
from PyQt5.QtCore import QCoreApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        self.setContentsMargins(10, 10, 10, 10)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        self.statusBar.showMessage("5초뒤 없어짐", 5000)

        group_box = QGroupBox('상태바')
        btn1 = QPushButton('상태바 보이기', self)
        btn2 = QPushButton('상태바 감추기', self)
        btn3 = QPushButton('상태바 텍스트 가져오기', self)
        btn4 = QPushButton('상태바 텍스트 변경하기', self)

        btn1.clicked.connect(self.onMyStatusBarShow)
        btn2.clicked.connect(self.onMyStatusBarHide)
        btn3.clicked.connect(self.onMyStatusBarGetText)
        btn4.clicked.connect(self.onMyStatusBarChangeText)

        v_box = QVBoxLayout()
        v_box.addWidget(btn1)
        v_box.addWidget(btn2)
        v_box.addWidget(btn3)
        v_box.addWidget(btn4)
        group_box.setLayout(v_box)

        self.setCentralWidget(group_box)

        self.setWindowTitle('Status Bar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onMyStatusBarShow(self):
        self.statusBar.showMessage('Ready')

    def onMyStatusBarHide(self):
        self.statusBar.clearMessage()

    def onMyStatusBarGetText(self):
        getMessage = self.statusBar.currentMessage()
        print(getMessage)

    def onMyStatusBarChangeText(self):
        self.statusBar.showMessage("change")


if __name__ == "__main__":
    app = QApplication([])  # app = QApplication(sys.argv) command line 매개변수가 있을 경우
    ex = MyApp()
    app.exec_()             # event loop 시작
