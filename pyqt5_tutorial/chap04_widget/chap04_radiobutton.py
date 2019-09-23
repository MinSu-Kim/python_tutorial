from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QCheckBox, QVBoxLayout, QRadioButton, QLabel, QButtonGroup


class MyRadioButton(QGroupBox):

    def __init__(self, parent):  # self는 MyApp 객체
        super().__init__()
        self.QMainWidow = parent
        self.setTitle('QRadioButton')

        rbtn1 = QRadioButton('QRadioButton', self)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.setText('Second Button')

        lbl = QLabel('')

        rbtn1.clicked.connect(lambda: lbl.setText(rbtn1.text()))
        rbtn2.clicked.connect(lambda: lbl.setText(rbtn2.text()))

        rbtn1.toggled.connect(lambda: self.QMainWidow.statusBar().showMessage('rbtn {}'.format(rbtn1.isChecked())))

        btn_group = QButtonGroup()
        btn_group.addButton(rbtn1)
        btn_group.addButton(rbtn2)

        vbox = QVBoxLayout()
        vbox.addWidget(rbtn1)
        vbox.addWidget(rbtn2)
        vbox.addWidget(lbl)

        self.setLayout(vbox)