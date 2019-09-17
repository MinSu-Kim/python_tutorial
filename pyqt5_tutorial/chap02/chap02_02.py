import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('../data/web.png'))    # setWindowIcon() 메서드는 어플리케이션 아이콘을 설정
        self.setGeometry(300, 300, 300, 200)            # setGeometry() 메서드는 창의 위치와 크기를 설정 move()와 resize() 메서드를 하나로 합쳐놓은 것과 같음
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    ex = MyApp()
    app.exec()