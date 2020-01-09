from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QCalendarWidget


class MyCalendar(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QCalendar Widget')
        self.init_ui()

    def init_ui(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        layout = QVBoxLayout()
        layout.addWidget(cal)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

    def showDate(self, date):
        self.lbl.setText(date.toString())