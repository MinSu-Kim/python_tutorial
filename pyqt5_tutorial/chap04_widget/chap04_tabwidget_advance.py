from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QTabWidget, QDialogButtonBox, QWidget, QTextBrowser, \
    QCheckBox, QComboBox, QLineEdit, QMessageBox


class MyTabWidgetAdv(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QTabWidget (심화)')
        self.init_ui()

    def init_ui(self):
        tabs = QTabWidget()
        tabs.addTab(FirstTab(), 'First')
        tabs.addTab(SecondTab(), 'Second')
        tabs.addTab(ThirdTab(), 'Third')

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(lambda : self.setTitle('QTabWidget (심화)'))
        buttonbox.rejected.connect(lambda : self.setTitle('QTabWidget - reject'))

        layout = QVBoxLayout()
        layout.addWidget(tabs)
        layout.addWidget(buttonbox)

        self.setLayout(layout)


class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        name = QLabel('Name:')
        nameedit = QLineEdit()
        age = QLabel('Age:')
        ageedit = QLineEdit()
        nation = QLabel('Nation:')
        nationedit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameedit)
        vbox.addWidget(age)
        vbox.addWidget(ageedit)
        vbox.addWidget(nation)
        vbox.addWidget(nationedit)
        vbox.addStretch()

        self.setLayout(vbox)


class SecondTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lan_group = QGroupBox('Select Your Language')
        combo = QComboBox()
        list = ['Korean', 'English', 'Chinese']
        combo.addItems(list)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(combo)
        lan_group.setLayout(vbox1)

        learn_group = QGroupBox('Select What You Want To Learn')
        korean = QCheckBox('Korean')
        english = QCheckBox('English')
        chinese = QCheckBox('Chinese')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(korean)
        vbox2.addWidget(english)
        vbox2.addWidget(chinese)
        learn_group.setLayout(vbox2)

        vbox = QVBoxLayout()
        vbox.addWidget(lan_group)
        vbox.addWidget(learn_group)
        self.setLayout(vbox)


class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl = QLabel('Terms and Conditions')
        text_browser = QTextBrowser()
        text_browser.setText('This is the terms and conditions')
        checkbox = QCheckBox('Check the terms and conditions.')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(text_browser)
        vbox.addWidget(checkbox)

        self.setLayout(vbox)