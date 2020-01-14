from PyQt5.QtWidgets import QGroupBox, QLabel, QLineEdit, QVBoxLayout, QApplication, QMainWindow


class MyLineEdit(QGroupBox):
    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.setTitle('QLineEdit')
        self.init_ui()

    def init_ui(self):
        self.label = QLabel('First Label', self)
        self.qle = QLineEdit(self)
        self.qle.textChanged.connect(self.onChanged)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.qle)

        self.setLayout(layout)

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication([])
    main = QMainWindow()
    main.setCentralWidget(MyLineEdit())
    main.show()
    app.exec_()