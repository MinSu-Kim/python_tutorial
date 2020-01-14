from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.statusBar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Absolute Layout')
        self.setGeometry(300, 300, 400, 200)

        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()
