from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTableView, QAbstractItemView

from pyqt5_tutorial.chap05_widget_view.TableModel import MyTableModel


class MyTableViewModelSimple02(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('Simple QTableView')
        self.init_ui()

    def init_ui(self):
        # create the view
        tableView = QTableView()
        data = [(1, 'aaa', 20, '대구'), (2, 'bbb', 30, '서울')]
        self.model = MyTableModel(data, ['번호', '이름', '나이', '주소'])
        tableView.setModel(self.model)

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
        hv = tableView.verticalHeader()
        hv.setVisible(True)

        # set horizontal header properties
        hh = tableView.horizontalHeader()
        hh.setStretchLastSection(True)

        self.fill_table_view([(3, 'aaa', 20, '대구'), (4, 'bbb', 30, '서울')])
        # set column width to fit contents
        # tableView.resizeColumnsToContents()
        # tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout = QVBoxLayout()
        layout.addWidget(tableView)

        self.setLayout(layout)

    def fill_table_view(self, data):
        for t in data:
            self.model.data.append(t)
            # self.model.data.insert(idx, t)
            self.model.layoutChanged.emit()