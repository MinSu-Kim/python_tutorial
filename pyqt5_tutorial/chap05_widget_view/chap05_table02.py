from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, QFrame, \
    QHeaderView, QHBoxLayout, QPushButton


class MySimpleTable01(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('Simple Table Widget 01')
        self.init_ui()

    def init_ui(self):
        self.table = QTableWidget(self)  # Create a table

        self.table.setColumnCount(3)  # Set three columns
        self.table.setRowCount(1)  # and one row

        font = QFont('FreeSans', 14)
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)  #  표 머리글 글꼴 설정

        self.table.setFrameShape(QFrame.NoFrame)  # 표식이 없는 아웃바운드 프레임 설정

        self.table.horizontalHeader().setFixedHeight(25) # Head 높이 설정
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # 2 열 너비 스크린 가득차도록 자동 조정
        self.table.horizontalHeader().setStretchLastSection(True)  # 마지막 열에서 최대까지 끌어서 놓기 설정

        self.table.horizontalHeader().resizeSection(0, 200)  # 첫번째 열의 너비를 200으로 설정

        # Set the table headers
        self.table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])

        # Set the tooltips to headings
        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        # Set the alignment to the headers
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignCenter)

        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 설정은 단일 셀 격자를 선택할 수 없으며 한 줄만 선택

        self.table.horizontalHeader().setStyleSheet('QHeaderView::section{background:green}')  # 배경색을 녹색

        # table.setColumnHidden(1, True)  # 두번째 열 숨김
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # 설정 양식 변경 불가
        self.table.setSortingEnabled(True)   # 설정 탭에서 자동 정렬 가능

        # table.horizontalHeader().setSectionsClickable(False)  # 표 머리글의 클릭을 금지

        # Fill the first line
        self.table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        self.table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))

        # Do the resize of the columns by content
        self.table.resizeColumnsToContents()

        #
        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.add_empty_item)

        addItemBtn = QPushButton('Item Add')
        addItemBtn.clicked.connect(self.table_appender)

        deleteBtn = QPushButton('select Remove')
        deleteBtn.clicked.connect(self.table_remove)

        layout_btn = QHBoxLayout()
        layout_btn.addWidget(addBtn)
        layout_btn.addWidget(addItemBtn)
        layout_btn.addWidget(deleteBtn)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(layout_btn)

        self.setLayout(layout)

    def add_empty_item(self):
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem('col 0'))
        self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem('col 1'))
        self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem('col 2'))

    def table_appender(self):
        def set_columns(len, pos):
            if pos == len - 1:
                self.table.setItem(self.table.rowCount() - 1, pos, QTableWidgetItem('aaaa %s' % self.table.rowCount()))
            else:
                self.table.setItem(self.table.rowCount() - 1, pos, QTableWidgetItem('bbb %s' % self.table.rowCount()))
                set_columns(len, pos + 1)

        self.table.insertRow(self.table.rowCount())
        set_columns(self.table.columnCount(), 0)

    def table_remove(self):
        selectedIndex = self.table.selectedIndexes()[0]
        # print(type(selectedIndex), selectedIndex.row())
        self.table.removeRow(selectedIndex.row())

