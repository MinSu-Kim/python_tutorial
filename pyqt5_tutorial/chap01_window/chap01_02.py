import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# 명령행 인수가 없다면  QApplication([])
# app = QApplication(sys.argv)
app = QApplication([])

# 모든 QWidget부모 (포함 위젯)하지 않고는 자신의 창의입니다. 이것은 창을 만드는 좋은 방법이지만
# 특정 QMainWindow클래스도 있습니다. 이것은 툴바, 상태 표시 줄 및 고정 가능한 위젯에 대한 지원을 포함하여
# 애플리케이션에서 기본 창으로 사용하기위한 몇 가지 장점이 있음

window = QMainWindow()
window.show()
# Start the event loop.
app.exec_()