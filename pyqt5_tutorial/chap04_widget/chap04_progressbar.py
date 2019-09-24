from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QGroupBox, QProgressBar, QPushButton, QVBoxLayout


class MyProgressBar(QGroupBox):
    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.setTitle('QProgressBar')
        self.init_ui()

    def init_ui(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        layout = QVBoxLayout()
        layout.addWidget(self.pbar)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)  # 타이머 이벤트를 실행하기 위해, start() 메서드를 호출합니다. 이 메서드는 두 개의 매개변수를 갖는데, 첫 번째는 종료시간이고 두 번째는 이벤트가 수행될 객체
            self.btn.setText('Stop')