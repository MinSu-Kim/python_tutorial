import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 명령행 인수가 없다면  QApplication([])
# app = QApplication(sys.argv)
app = QApplication([])
window = QWidget()
window.show()

app.exec_()  # Qt로 제어권을 넘겨 '사용자가 닫을 때까지 응용 프로그램을 실행'하도록 요청
