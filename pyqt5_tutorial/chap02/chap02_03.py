from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolTip
from PyQt5.QtCore import QCoreApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        # 여백 지정
        self.setContentsMargins(20, 20, 20, 20)

        # 툴팁에 사용될 폰트를 설정
        QToolTip.setFont(QFont('SansSerif', 10))
        # 메인 창의 툴팁 설정
        self.setToolTip('This is a <b>QMainWindow</b> widget')

        # 생성자(QPushButton())의 첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력
        # 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력
        btn = QPushButton('Quit', self)
        # 버튼에 툴팁 설정
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.move(50, 50)
        # btn.resize(btn.sizeHint())
        self.setCentralWidget(btn)
        # 버튼(btn)을 클릭하면 'clicked' 시그널이 만들어집니다.
        # instance() 메서드는 현재 인스턴스를 반환합니다.
        # 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됩니다.
        # 이렇게 발신자(Sender)와 수신자(Receiver), 두 객체 간에 커뮤니케이션이 이루어집니다.
        # 이 예제에서 발신자는 푸시버튼(btn)이고, 수신자는 어플리케이션 객체(app)입니다.
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication([])  # app = QApplication(sys.argv) command line 매개변수가 있을 경우
    ex = MyApp()
    app.exec_()             # event loop 시작
