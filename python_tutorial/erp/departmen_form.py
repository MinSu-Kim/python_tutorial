import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


class DepartmentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("department.ui")
        self.ui.table.setHorizontalHeaderLabels(["부서번호", "부서명", "위치"])
        self.ui.show()

    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):
            item_no = QTableWidgetItem()
            item_no.setData(Qt.DisplayRole, no)
            self.ui.table.setItem(idx, 0, item_no)
            self.ui.table.setItem(idx, 1, QTableWidgetItem(name))
            item_floor = QTableWidgetItem()
            item_floor.setData(Qt.DisplayRole, floor)
            self.ui.table.setItem(idx, 2, QTableWidgetItem(item_floor))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = DepartmentForm()
    data = [(1, "마케팅", 8), (2, "개발", 10), (3, "인사", 20)]
    w.load_data(data)
    sys.exit(app.exec())
