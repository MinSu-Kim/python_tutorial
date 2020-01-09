from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QPushButton


class MyPushButton(QGroupBox):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.setTitle('QPushButton')

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
        self.setLayout(vbox)

    def change_toggle(self):
        if self.push_btn02.isEnabled():
            self.push_btn02.setEnabled(False)
        else:
            self.push_btn02.setEnabled(True)
