from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout, QInputDialog, \
    QColorDialog, QSizePolicy, QFontDialog, QAction, QTextEdit, QFileDialog, QMessageBox


class MyDialogs(QGroupBox):

    def __init__(self, parent):
        super().__init__()
        self.QMainWidow = parent
        self.setTitle('대화 상자')
        self.init_ui()

    def init_ui(self):
        layout_input = self.create_input_dlg()
        layout_color = self.create_color_dlg()
        layout_font = self.create_font_dlg()
        layout_file = self.create_file_dlg()
        layout_msg = self.create_msg_dlg()

        layout = QVBoxLayout()
        layout.addLayout(layout_input)
        layout.addLayout(layout_color)
        layout.addLayout(layout_font)
        layout.addLayout(layout_msg)
        layout.addLayout(layout_file)
        self.setLayout(layout)

    def create_input_dlg(self):
        label_input = QLabel('QInputDialog', self)
        self.btn_input = QPushButton('Dialog', self)
        self.le_input = QLineEdit(self)
        self.btn_input.clicked.connect(self.show_input_dialog)

        layout_input = QHBoxLayout()
        layout_input.addWidget(label_input)
        layout_input.addWidget(self.le_input)
        layout_input.addWidget(self.btn_input)
        return layout_input

    def create_color_dlg(self):
        self.label_color = QLabel('QColorDialog')
        self.label_color.setStyleSheet('QWidget { background-color: %s }' % QColor(66, 66, 66).name())

        btn_color = QPushButton('Dialog')
        le_color = QLineEdit()
        btn_color.clicked.connect(self.show_color_dialog)

        layout_color = QHBoxLayout()
        layout_color.addWidget(self.label_color)
        layout_color.addWidget(le_color)
        layout_color.addWidget(btn_color)
        return layout_color

    def create_font_dlg(self):
        label_font = QLabel('QFontDialog', self)
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.clicked.connect(self.show_font_dlg)
        self.lbl_msg = QLabel('The quick brown fox jumps over the lazy dog', self)

        layout_font = QHBoxLayout()
        layout_font.addWidget(label_font)
        layout_font.addWidget(btn)
        layout_font.addWidget(self.lbl_msg)
        return layout_font

    def create_file_dlg(self):
        self.textEdit = QTextEdit()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        self.QMainWidow.menubar = self.QMainWidow.menuBar()
        self.QMainWidow.menubar.setNativeMenuBar(False)
        fileMenu = self.QMainWidow.menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        file_open_button = QPushButton('File Open')
        file_open_button.clicked.connect(self.showDialog)

        layout_file = QVBoxLayout()
        layout_file.addWidget(file_open_button)
        layout_file.addWidget(self.textEdit)
        return layout_file

    def create_msg_dlg(self):
        label = QLabel('QMessageBox', self)
        btn = QPushButton('Dialog', self)
        btn.clicked.connect(self.show_msg_dlg)
        self.lbl_msg = QLabel('QMessageBox Response')

        layout_msg = QHBoxLayout()
        layout_msg.addWidget(label)
        layout_msg.addWidget(self.lbl_msg)
        layout_msg.addWidget(btn)

        return layout_msg

    def show_input_dialog(self):
        # 두 번째 매개변수는 대화창의 타이틀, 세 번째 매개변수는 대화창 안에 보여질 메세지
        # 입력 대화창은 입력한 텍스트와 불(Boolean) 값을 반환.
        # 텍스트를 입력한 후 'OK' 버튼을 누르면 불 값은 True, 'Cancel' 버튼을 누르면 불 값은 False를 반환
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le_input.setText(str(text))
        else:
            self.le_input.clear()
            self.le_input.setFocus()

    def show_color_dialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.label_color.setStyleSheet('QWidget { background-color: %s }' % col.name())

    def show_font_dlg(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl_msg.setFont(font)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def show_msg_dlg(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.lbl_msg.setText("Yes")
        else:
            self.lbl_msg.setText('No')

