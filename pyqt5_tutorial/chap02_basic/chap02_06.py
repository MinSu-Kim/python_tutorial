from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMessageBox


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.toolbar = self.addToolBar('toolBar')
        self.statusBar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('My First Application')  # 타이틀바에 나타나는 창의 제목을 설정
        self.setGeometry(300, 300, 400, 200)

        exit_action = QAction(QIcon('icon/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        edit_action = QAction(QIcon('icon/edit.png'), 'Edit', self)
        edit_action.setShortcut('Ctrl+E')
        edit_action.setStatusTip('Edit application')
        edit_action.triggered.connect(lambda x: QMessageBox.about(self, 'Title', edit_action.text()))

        print_action = QAction(QIcon('icon/print.png'), 'Print', self)
        print_action.setShortcut('Ctrl+P')
        print_action.setStatusTip('Prinit application')
        print_action.triggered.connect(lambda x: QMessageBox.about(self, print_action.text(), print_action.text()))

        save_action = QAction(QIcon('icon/save.png'), 'Save', self)
        save_action.setStatusTip('Save application')
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(lambda x: QMessageBox.about(self, save_action.text(), save_action.text()))

        self.toolbar.addAction(save_action)
        self.toolbar.addAction(exit_action)
        self.toolbar.addAction(edit_action)
        self.toolbar.addAction(print_action)


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()
