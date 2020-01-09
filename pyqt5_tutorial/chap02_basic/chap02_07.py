from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.statusBar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('My First Application')  # 타이틀바에 나타나는 창의 제목을 설정
        self.resize(400, 200)

        cur_loc = self.frameGeometry()
        print('cur_loc', cur_loc)
        center_loc = QDesktopWidget().availableGeometry().center()
        cur_loc.moveCenter(center_loc)
        self.move(cur_loc.topLeft())
        print('current_location {0} \ncenter_loc {1} \ncenter_loc.topLeft {2}'.format(cur_loc, center_loc, cur_loc.topLeft()))


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()
