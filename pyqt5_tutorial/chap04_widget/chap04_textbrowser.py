from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QLineEdit, QTextBrowser, QPushButton


class MyTextBrowser(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QTextBrowser')
        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)

        self.init_text()

        layout = QVBoxLayout()
        layout.addWidget(self.le)
        layout.addWidget(self.tb)
        layout.addWidget(self.clear_btn)

        self.setLayout(layout)

    def init_text(self):
        texts = [
            '<i>Italic</i>',
            '<p style="color: red">Red</p>',
            '<p style="font-size: 20px">20px</p>',
            '<a href="https://www.naver.com">Naver</a>']
        for t in texts:
            self.tb.append(t)

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()
