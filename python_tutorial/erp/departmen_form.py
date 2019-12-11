import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QAbstractItemView


class DepartmentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("department.ui")
        self.ui.table.setHorizontalHeaderLabels(["부서번호", "부서명", "위치"])
        self.ui.show()
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # # row단위 선택
        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)# 셀 내용 수정불가

        self.ui.addBtn.clicked.connect(self.addItem)
        self.ui.updateBtn.clicked.connect(self.updateItem)
        self.ui.delBtn.clicked.connect(self.delItem)
        self.ui.clearBtn.clicked.connect(self.clearItem)

    def clearItem(self):
        self.ui.leDeptNo.clear()
        self.ui.leDeptName.clear()
        self.ui.leFloor.clear()

    def updateItem(self):
        selectedIndex = self.ui.table.selectedIndexes()[0]

        item_no = self.ui.table.item(selectedIndex.row(), 0)
        item_name = self.ui.table.item(selectedIndex.row(), 1)
        item_floor = self.ui.table.item(selectedIndex.row(), 2)

        self.ui.leDeptNo.setText(item_no.text())
        self.ui.leDeptName.setText(item_name.text())
        self.ui.leFloor.setText(item_floor.text())

    def delItem(self):
        selectedIndex = self.ui.table.selectedIndexes()[0]
        self.ui.table.removeRow(selectedIndex.row())

    def addItem(self):
        no = self.ui.leDeptNo.text()
        name = self.ui.leDeptName.text()
        floor = self.ui.leFloor.text()

        item_no = QTableWidgetItem()
        item_no.setData(Qt.DisplayRole, no)
        item_no.setTextAlignment(Qt.AlignCenter)

        item_name = QTableWidgetItem()
        item_name.setData(Qt.DisplayRole, name)
        item_name.setTextAlignment(Qt.AlignCenter)

        item_floor = QTableWidgetItem()
        item_floor.setData(Qt.DisplayRole, floor)
        item_floor.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

        currentRowCount = self.ui.table.rowCount()  # necessary even when there are no rows in the table
        self.ui.table.insertRow(currentRowCount)
        self.ui.table.setItem(currentRowCount, 0, item_no)
        self.ui.table.setItem(currentRowCount, 1, item_name)
        self.ui.table.setItem(currentRowCount, 2, item_floor)


    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):
            item_no = QTableWidgetItem()
            item_no.setData(Qt.DisplayRole, no)
            item_no.setTextAlignment(Qt.AlignCenter)

            item_name = QTableWidgetItem()
            item_name.setData(Qt.DisplayRole, name)
            item_name.setTextAlignment(Qt.AlignCenter)

            item_floor = QTableWidgetItem()
            item_floor.setData(Qt.DisplayRole, floor)
            item_floor.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self.ui.table.setItem(idx, 0, item_no)
            self.ui.table.setItem(idx, 1, item_name)
            self.ui.table.setItem(idx, 2, item_floor)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = DepartmentForm()
    data = [(1, "마케팅", 8), (2, "개발", 10), (3, "인사", 20)]
    w.load_data(data)
    sys.exit(app.exec())
