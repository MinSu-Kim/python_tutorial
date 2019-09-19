from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QHBoxLayout, QWidget, QCheckBox, QVBoxLayout, QComboBox, \
    QListWidget, QLineEdit


class MyWidgets(QWidget):
    def __init__(self):
        super().__init__()

        lbl = QLabel("Hello")
        # 글꼴 팁 위젯 글꼴의 속성을 변경하려면 일반적으로 현재 글꼴 을 가져 와서 업데이트 한 다음 다시 적용하는 것이 좋습니다.
        # 이렇게하면 글꼴 모양이 데스크탑 규칙에 맞게 유지됩니다.
        font = lbl.font()
        font.setPointSize(30)
        lbl.setFont(font)
        lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        lblImg = QLabel()
        lblImg.setPixmap(QPixmap('../../data/web.png'))
        lblImg.setScaledContents(True)  # 가로 세로 비율을 유지하면서 크기가 조정
        lblImg.setAlignment(Qt.AlignCenter)

        hbox01 = QHBoxLayout()
        hbox01.addStretch(1)
        hbox01.addWidget(lbl)
        hbox01.addStretch(1)
        hbox01.addWidget(lblImg)
        hbox01.addStretch(1)

        qcheckBox = QCheckBox()
        qcheckBox.setCheckState(Qt.Checked)
        qcheckBox.stateChanged.connect(self.show_state)

        qcombox = QComboBox()
        qcombox.addItems(['One', 'Two', 'Three'])
        # The default signal from currentIndexChanged sends the index
        qcombox.currentIndexChanged.connect(self.index_changed)
        # The same signal can send a text string
        qcombox.currentIndexChanged[str].connect(self.text_changed)

        qcombox2 = QComboBox()
        qcombox2.setEditable(True)
        qcombox2.setInsertPolicy(QComboBox.InsertAtBottom)
        qcombox2.setMaxCount(5)

        qList = QListWidget()
        qList.addItems(["One", "Two", "Three"])

        # In QListWidget there are two separate signals for the item, and the str
        qList.currentItemChanged.connect(self.list_index_changed)
        qList.currentTextChanged.connect(self.list_text_changed)

        hbox02 = QHBoxLayout()
        hbox02.addStretch(1)
        hbox02.addWidget(qcheckBox)
        hbox02.addStretch(1)
        hbox02.addWidget(qcombox)
        hbox02.addStretch(1)
        hbox02.addWidget(qcombox2)
        hbox02.addStretch(1)
        hbox02.addWidget(qList)
        hbox02.addStretch(1)

        self._lineEdit = QLineEdit()
        self._lineEdit.setMaxLength(10)
        self._lineEdit.setPlaceholderText("Enter your text")

        # widget.setReadOnly(True) # uncomment this to make readonly

        self._lineEdit.returnPressed.connect(self.line_edit_return_pressed)
        self._lineEdit.selectionChanged.connect(self.line_edit_selection_changed)
        self._lineEdit.textChanged.connect(self.line_edit_text_changed)
        self._lineEdit.textEdited.connect(self.line_edit_text_edited)

        self._lblResult = QLabel()

        hbox03 = QHBoxLayout()
        hbox03.addStretch(1)
        hbox03.addWidget(self._lineEdit)
        hbox03.addStretch(1)
        hbox03.addWidget(self._lblResult)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox01)
        vbox.addLayout(hbox02)
        vbox.addLayout(hbox03)

        self.setLayout(vbox)

    def show_state(self, state):
        print(state == Qt.Checked)
        print(state)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

    def list_index_changed(self, i):
        print(i.text())

    def list_text_changed(self, s):
        print(s)

    def line_edit_return_pressed(self):
        print("Return pressed!")
        self._lblResult.setText("BOOM!")

    def line_edit_selection_changed(self):
        print("Selection changed")
        print(self._lineEdit.selectedText())

    def line_edit_text_changed(self, s):
        print("Text changed...")
        print(s)

    def line_edit_text_edited(self, s):
        print("Text edited...")
        print(s)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        myWidget = MyWidgets()
        self.setCentralWidget(myWidget)  # self.setLayout(hbox)  # QHBoxLayout, QVBoxLayout 같은 layout 사용못함
        self.setGeometry(300, 700, 350, 150)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
