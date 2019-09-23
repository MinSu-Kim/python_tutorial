from PyQt5.QtWidgets import QComboBox, QGroupBox, QLabel, QPushButton, QHBoxLayout


class MyComboBox(QGroupBox):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.setTitle('QComboBox')
        self.init_ui()

    def init_ui(self):
        lbl = QLabel()

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.activated[str].connect(lambda x: lbl.setText(x))

        push_item = QPushButton('Add')
        push_item.clicked.connect(lambda x: cb.addItem('add'))

        hbox = QHBoxLayout()
        hbox.addWidget(cb)
        hbox.addWidget(lbl)
        hbox.addWidget(push_item)

        self.setLayout(hbox)