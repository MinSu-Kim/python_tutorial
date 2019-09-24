from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QWidget, QTabWidget


class MyTabWidget(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('제목')
        self.init_ui()

    def init_ui(self):
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        layout = QVBoxLayout()
        layout.addWidget(tabs)

        self.setLayout(layout)