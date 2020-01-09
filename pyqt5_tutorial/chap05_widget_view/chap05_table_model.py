from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTableView, QAbstractItemView, QTableWidgetItem


class MyTableViewModelSimple01(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('Simple QTableView')
        self.init_ui()

    def init_ui(self):
        # create the view
        tableView = QTableView()
        self.model = QStandardItemModel(0, 4)  # 0행 4열의 모델 정의
        self.model.setHorizontalHeaderLabels(['번호', '이름', '나이', '주소'])
        tableView.setModel(self.model)

        # set the minimum size
        # tableView.setMinimumSize(400, 300)

        # header size

        tableView.horizontalHeader().resizeSection(0, 20)
        tableView.horizontalHeader().resizeSection(1, 60)
        tableView.horizontalHeader().resizeSection(2, 100)

        tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 녹색

        # Set the alignment to the headers
        tableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # 셀 내용 수정불가
        tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # hide grid
        tableView.setShowGrid(True)

        # row단위 선택
        tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # hide vertical header
        vh = tableView.verticalHeader()
        vh.setVisible(True)

        # set horizontal header properties
        hh = tableView.horizontalHeader()
        hh.setStretchLastSection(True)

        self.fill_table_view([(1, 'aaa', 20, '대구'), (2, 'bbb', 30, '서울')])

        # set column width to fit contents
        # tableView.resizeColumnsToContents()
        # tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout = QVBoxLayout()
        layout.addWidget(tableView)

        self.setLayout(layout)

    def fill_table_view(self, data):

        for idx, (no, name, age, addr) in enumerate(data):
            item_no = QStandardItem(str(no))
            item_name = QStandardItem(name)
            item_age = QStandardItem(str(age))
            item_addr = QStandardItem(addr)

            item_no.setTextAlignment(Qt.AlignCenter)
            item_name.setTextAlignment(Qt.AlignCenter)
            item_age.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_addr.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            self.model.insertRow(idx, (item_no,item_name, item_age, item_addr))
            # self.model.appendRow((item_no,item_name, item_age, item_addr))
