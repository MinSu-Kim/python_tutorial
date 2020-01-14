from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel


class MyPixmap(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QPixmap')
        self.init_ui()

    def init_ui(self):
        pixmap = QPixmap('python.png')
        pixmap.scaledToWidth(200)

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_img.setAlignment(Qt.AlignCenter)

        lbl_size = QLabel('Width: ' + str(pixmap.width()) + ', Height: ' + str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(lbl_img)
        layout.addWidget(lbl_size)

        self.setLayout(layout)
