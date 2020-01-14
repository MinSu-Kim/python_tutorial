from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QCheckBox, QVBoxLayout


class MyCheckBox(QGroupBox):

    def __init__(self, parent):  # self는 MyApp 객체
        super().__init__()
        self.QMainWidow = parent
        self.init_ui()

    def init_ui(self):
        self.setTitle('QCheckBox')

        check_box01 = QCheckBox('Show title', self)
        check_box01.toggle()
        check_box01.stateChanged.connect(self.changeTitle)

        check_box02 = QCheckBox('Tristate', self)
        check_box02.setTristate(True)
        check_box02.stateChanged.connect(self.prnState)

        vbox = QVBoxLayout()
        vbox.addWidget(check_box01)
        vbox.addWidget(check_box02)
        self.setLayout(vbox)

    def prnState(self, state):
        self.QMainWidow.statusBar().showMessage('state : {}'.format(state))

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.QMainWidow.setWindowTitle('QCheckBox')
        else:
            self.QMainWidow.setWindowTitle(' ')