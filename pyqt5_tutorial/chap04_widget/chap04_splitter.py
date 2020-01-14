from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QHBoxLayout, QFrame, QSplitter


class MySplitter(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QSplitter')
        self.init_ui()

    def init_ui(self):
        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        layout = QHBoxLayout()
        layout.addWidget(splitter2)

        self.setLayout(layout)