from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QApplication, QGroupBox, QVBoxLayout

from pyqt5_tutorial.signal_slot.signal_study01 import MySignalSlot01


class SignalSlotApp(QMainWindow):
    def __init__(self):
        super(SignalSlotApp, self).__init__()
        self.statusBar()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Signal Slot Study')
        self.setGeometry(0, 0, 800, 600)

        h_box01 = QHBoxLayout()
        h_box01.addWidget(MySignalSlot01())
        group01 = QGroupBox()
        group01.setTitle("Basic Signal And Slot")
        group01.setLayout(h_box01)

        root_layout = QVBoxLayout()
        root_layout.addWidget(group01)

        widget = QWidget()
        widget.setLayout(root_layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = SignalSlotApp()
    ex.show()
    app.exec_()