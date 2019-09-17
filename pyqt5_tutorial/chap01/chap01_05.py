from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()
        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
