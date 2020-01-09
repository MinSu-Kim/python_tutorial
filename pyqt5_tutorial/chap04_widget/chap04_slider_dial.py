from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QSlider, QDial, QPushButton


class MySliderDial(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QSlider & QDial')
        self.init_ui()

    def init_ui(self):
        # Qt.Horizontal, Qt.Vertical 수평 또는 수직 방향 설정
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 50)   # setRange() 메서드로 값의 범위를 0에서 50까지로 설정
        self.slider.setSingleStep(2)  # setSingleStep() 메서드는 조절 가능하는 최소 단위를 설정

        self.dial = QDial(self)
        self.dial.setRange(0, 50)

        btn = QPushButton('Default', self)

        # 슬라이더와 다이얼의 값이 변할 때 발생하는 시그널을 각각 다이얼과 슬라이더의 값을 조절해주는
        # 메서드 (setValue)에 서로 연결함으로써 두 위젯의 값이 언제나 일치하도록 해줍니다.
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)

        btn.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.dial)
        layout.addWidget(btn)

        self.setLayout(layout)

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)