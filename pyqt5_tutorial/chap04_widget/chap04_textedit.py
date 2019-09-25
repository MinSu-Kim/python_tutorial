from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QTextEdit


class MyTextEdit(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QTextEdit')
        self.init_ui()

    def init_ui(self):
        lbl = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl = QLabel('The number of words is 0')

        self.te.textChanged.connect(self.text_changed)

        layout = QVBoxLayout()
        layout.addWidget(lbl)
        layout.addWidget(self.te)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl.setText('The number of words is ' + str(len(text.split())))

