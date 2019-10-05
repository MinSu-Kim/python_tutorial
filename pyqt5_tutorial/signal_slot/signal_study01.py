# 다이얼의 값이 변할 때 발생하는 시그널이 LCD 화면에 숫자를 표시하는 슬롯과 연결
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout


class MySignalSlot01(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)  # LCD 화면과 같이 숫자를 표시
        dial = QDial(self)      # QDial은 다이얼을 회전해서 값을 조절하는 위젯

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

