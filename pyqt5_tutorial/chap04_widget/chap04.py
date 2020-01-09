from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QMainWindow, QApplication, QScrollArea

from pyqt5_tutorial.chap04_widget.chap04_calendar import MyCalendar
from pyqt5_tutorial.chap04_widget.chap04_checkbox import MyCheckBox
from pyqt5_tutorial.chap04_widget.chap04_combobox import MyComboBox
from pyqt5_tutorial.chap04_widget.chap04_dialog import MyDialogs
from pyqt5_tutorial.chap04_widget.chap04_groupbox import MyGroupBox
from pyqt5_tutorial.chap04_widget.chap04_label import MyLabel
from pyqt5_tutorial.chap04_widget.chap04_line_edit2 import MyLineEditTest
from pyqt5_tutorial.chap04_widget.chap04_lineedit import MyLineEdit
from pyqt5_tutorial.chap04_widget.chap04_pixmap import MyPixmap
from pyqt5_tutorial.chap04_widget.chap04_progressbar import MyProgressBar
from pyqt5_tutorial.chap04_widget.chap04_pushbutton import MyPushButton
from pyqt5_tutorial.chap04_widget.chap04_radiobutton import MyRadioButton
from pyqt5_tutorial.chap04_widget.chap04_slider_dial import MySliderDial
from pyqt5_tutorial.chap04_widget.chap04_spinbox import MySpinBox
from pyqt5_tutorial.chap04_widget.chap04_splitter import MySplitter
from pyqt5_tutorial.chap04_widget.chap04_tab import MyTabWidget
from pyqt5_tutorial.chap04_widget.chap04_tabwidget_advance import MyTabWidgetAdv
from pyqt5_tutorial.chap04_widget.chap04_textbrowser import MyTextBrowser
from pyqt5_tutorial.chap04_widget.chap04_textedit import MyTextEdit


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.statusBar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QWidgets')  # 타이틀바에 나타나는 창의 제목을 설정
        self.setGeometry(0, 0, 1170, 700)

        h_box01 = QHBoxLayout()
        h_box01.addWidget(MyPushButton())
        h_box01.addWidget(MyCheckBox(self))
        h_box01.addWidget(MyRadioButton(self))
        h_box01.addWidget(MyComboBox())
        h_box01.addWidget(MyLabel())
        h_box01.addWidget(MyLineEdit())

        h_box02 = QHBoxLayout()
        h_box02.addWidget(MyProgressBar())
        h_box02.addWidget(MySliderDial())
        h_box02.addWidget(MySplitter())
        h_box02.addWidget(MyLineEditTest())
        h_box02.addWidget(MyGroupBox())

        h_box03 = QHBoxLayout()
        h_box03.addWidget(MyTabWidget())
        h_box03.addWidget(MyTabWidgetAdv())
        h_box03.addWidget(MyCalendar())
        h_box03.addWidget(MySpinBox())

        h_box04 = QHBoxLayout()
        h_box04.addWidget(MyTextBrowser())
        h_box04.addWidget(MyTextEdit())
        h_box04.addWidget(MyDialogs(self))
        h_box04.addStretch(2)

        v_box = QVBoxLayout()
        v_box.addWidget(MyPixmap())
        v_box.addLayout(h_box01)
        v_box.addLayout(h_box02)
        v_box.addLayout(h_box03)
        v_box.addLayout(h_box04)

        widget = QWidget()
        widget.setLayout(v_box)

        scrollArea = QScrollArea()
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidget(widget)

        self.setCentralWidget(scrollArea)


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()
