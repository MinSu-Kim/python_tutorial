import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 필요한 부분들을 load 기본적인 UI 구성요소를 제공하는 위젯(클래스)들은 PyQt5.QtWidgets 모듈에 포함됨


class MyApp(QWidget):

    def __init__(self):     # self는 MyApp 객체
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')    # 타이틀바에 나타나는 창의 제목을 설정
        self.move(300, 300)                            # 위젯을 스크린의 x=300px, y=300px의 위치로 이동
        self.resize(400, 200)                          # 위젯의 크기를 너비 400px, 높이 200px로 조절
        self.show()                                    # 위젯을 스크린에 보여줌


# '__name__'은 현재 모듈의 이름이 저장되는 내장 변수.
# 만약 'moduleA.py'라는 코드를 import해서 예제 코드를 수행하면 __name__ 은 'moduleA'가 되며 코드를 직접 실행하면 __name__ 은 __main__이 됨.
# 아래 한 줄의 코드를 통해 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지를 확인.
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    sys.exit(app.exec_())