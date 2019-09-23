import PyQt5.QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QMainWindow

from pyqt5_tutorial.chap04_widget.chap04_checkbox import MyCheckBox
from pyqt5_tutorial.chap04_widget.chap04_combobox import MyComboBox
from pyqt5_tutorial.chap04_widget.chap04_label import MyLabel
from pyqt5_tutorial.chap04_widget.chap04_pushbutton import MyPushButton
from pyqt5_tutorial.chap04_widget.chap04_radiobutton import MyRadioButton


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.statusBar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QCheckBox')  # 타이틀바에 나타나는 창의 제목을 설정
        self.setGeometry(300, 300, 400, 200)

        h_box01 = QHBoxLayout()
        h_box01.addWidget(MyPushButton())
        h_box01.addWidget(MyCheckBox(self))
        h_box01.addWidget(MyRadioButton(self))

        h_box02 = QHBoxLayout()
        h_box02.addWidget(MyComboBox())
        h_box02.addWidget(MyLabel())

        v_box = QVBoxLayout()
        v_box.addLayout(h_box01)
        v_box.addLayout(h_box02)

        widget = QWidget()
        widget.setLayout(v_box)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()
