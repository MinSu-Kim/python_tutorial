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

        get_cmb_items_btn = QPushButton('Get Items')
        get_cmb_items_btn.clicked.connect(lambda stat, cmb=cb:self.get_items(stat, cmb))

        hbox = QHBoxLayout()
        hbox.addWidget(cb)
        hbox.addWidget(lbl)
        hbox.addWidget(push_item)
        hbox.addWidget(get_cmb_items_btn)

        self.setLayout(hbox)

    def get_items(self, stat, cmb):
        aaa = cmb.findText('Option3')
        print(type(aaa), aaa)

