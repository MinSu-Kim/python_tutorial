from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QTableView, QHeaderView


class MyTableViewModelSimple(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('Simple QTableView')
        self.init_ui()

    def init_ui(self):
        self.model = QStandardItemModel(4, 4)  # 4행 4열의 모델 정
        self.model.setHorizontalHeaderLabels(['번호', '이름', '나이', '주소'])

        for row in range(4):
            for column in range(4):
                i = QStandardItem("row %s,column %s" % (row, column))
                i.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(row, column, i)

        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # self.tableView.horizontalHeader().setStretchLastSection(True)  # 마지막 열은 남은 경계면을 채우기
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)##  모든 열은 자동으로 당겨져서 경계면이 가득채우

        layout = QVBoxLayout()
        layout.addWidget(self.tableView)

        self.setLayout(layout)

