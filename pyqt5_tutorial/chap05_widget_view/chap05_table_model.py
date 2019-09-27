from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTableView, QAbstractItemView

from pyqt5_tutorial.chap05_widget_view.TableModel import MyTableModel


class MyTableViewModelAdvance(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('Simple QTableView')
        self.init_ui()

    def init_ui(self):
        # create the view
        tableView = QTableView()

        # set the table model
        header = ['번호', '이름', '나이', '주소']
        data = [(1, 'aaa', 20, '대구'), ((2, 'bbb', 30, '서울'))]
        # data = [()]
        tm = MyTableModel(data, header)
        tableView.setModel(tm)
        # set the minimum size
        tableView.setMinimumSize(400, 300)

        # header size
        tableView.horizontalHeader().resizeSection(0, 20)
        tableView.horizontalHeader().resizeSection(1, 60)
        tableView.horizontalHeader().resizeSection(2, 100)

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
        vh.setVisible(False)

        # set horizontal header properties
        hh = tableView.horizontalHeader()
        hh.setStretchLastSection(True)

        # 테이블 내용 정렬하는 방법 찾기
        
        # set column width to fit contents
        # tableView.resizeColumnsToContents()
        # tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        layout = QVBoxLayout()
        layout.addWidget(tableView)

        self.setLayout(layout)

