from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QPushButton, QApplication


class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):

    # def __init__ etc.
    # ... not shown for clarity
    def onMyToolBarButtonClick(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        if dlg.exec_():
            print("success!")
        else:
            print("Cancel!")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    window.onMyToolBarButtonClick('test')
    app.exec_()