from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QLabel("Hello")
        # 글꼴 팁 위젯 글꼴의 속성을 변경하려면 일반적으로 현재 글꼴 을 가져 와서 업데이트 한 다음 다시 적용하는 것이 좋습니다.
        # 이렇게하면 글꼴 모양이 데스크탑 규칙에 맞게 유지됩니다.
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)

        
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()