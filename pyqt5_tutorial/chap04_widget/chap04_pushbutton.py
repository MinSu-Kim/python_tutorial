from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QPushButton


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.statusBar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('My First Application')  # 타이틀바에 나타나는 창의 제목을 설정
        self.setGeometry(300, 300, 400, 200)
        self.setCentralWidget(self.create_group_pushbutton())

    def create_group_pushbutton(self):
        groupbox = QGroupBox('QPushButton')

        push_btn01= QPushButton('&Button1', self)  # shortcut Alt+b
        push_btn01.setCheckable(True)
        push_btn01.toggle()
        push_btn01.clicked.connect(lambda x:self.statusBar().showMessage(push_btn01.text()))

        self.push_btn02 = QPushButton(self)
        self.push_btn02.setText('Button&2')  # shortcut Alt+2
        self.push_btn02.setEnabled(False)
        self.push_btn02.toggled.connect(lambda x:self.statusBar().showMessage(self.push_btn02.text()))

        push_btn03 = QPushButton('&Change PushButton2')
        push_btn03.pressed.connect(self.change_toggle)

        push_btn04 = QPushButton('Push Button01 Toggle')
        push_btn04.released.connect(lambda : push_btn01.toggle())

        vbox = QVBoxLayout()
        vbox.addWidget(push_btn01)
        vbox.addWidget(self.push_btn02)
        vbox.addWidget(push_btn03)
        vbox.addWidget(push_btn04)
        groupbox.setLayout(vbox)

        return groupbox

    def change_toggle(self):
        if self.push_btn02.isEnabled():
            self.push_btn02.setEnabled(False)
        else:
            self.push_btn02.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()
