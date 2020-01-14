from PyQt5.QtCore import QDate, Qt, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget


class MyApp(QMainWindow):

    def __init__(self):  # self는 MyApp 객체
        super().__init__()
        self.statusBar().showMessage(QDate.currentDate().toString(Qt.DefaultLocaleLongDate))
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QDate, QTime, QDateTime Application')  # 타이틀바에 나타나는 창의 제목을 설정
        self.setGeometry(300, 300, 500, 200)

        hbox = QHBoxLayout()
        hbox.addWidget(self.create_gb_qdate())
        hbox.addWidget(self.create_db_qtime())
        hbox.addWidget(self.create_db_date_time())
        widget = QWidget()
        widget.setLayout(hbox)

        self.setCentralWidget(widget)

    def create_db_date_time(self):
        groupbox = QGroupBox('QDate & Time')

        date_time = QDateTime.currentDateTime()

        lbl01 = QLabel(date_time.toString())
        lbl02 = QLabel(date_time.toString('yyyy-MM-dd hh:mm:ss A'))
        lbl03 = QLabel(date_time.toString(Qt.DefaultLocaleLongDate))
        lbl04 = QLabel(date_time.toString(Qt.DefaultLocaleShortDate))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl01)
        vbox.addWidget(lbl02)
        vbox.addWidget(lbl03)
        vbox.addWidget(lbl04)
        groupbox.setLayout(vbox)

        return groupbox

    def create_db_qtime(self):
        groupbox = QGroupBox('QTime')

        time = QTime.currentTime()

        lbl01 = QLabel(time.toString())
        lbl02 = QLabel(time.toString('hh:mm:ss A'))
        lbl03 = QLabel(time.toString(Qt.DefaultLocaleLongDate))
        lbl04 = QLabel(time.toString(Qt.DefaultLocaleShortDate))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl01)
        vbox.addWidget(lbl02)
        vbox.addWidget(lbl03)
        vbox.addWidget(lbl04)
        groupbox.setLayout(vbox)

        return groupbox


    def create_gb_qdate(self):
        groupbox = QGroupBox('QDate')

        now = QDate.currentDate()

        lbl01 = QLabel(now.toString())
        lbl02 = QLabel(now.toString('yyyy-MM-dd'))
        lbl03 = QLabel(now.toString(Qt.DefaultLocaleLongDate))
        lbl04 = QLabel(now.toString(Qt.ISODate))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl01)
        vbox.addWidget(lbl02)
        vbox.addWidget(lbl03)
        vbox.addWidget(lbl04)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == '__main__':
    app = QApplication([])  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합
    ex = MyApp()
    ex.show()
    app.exec_()
