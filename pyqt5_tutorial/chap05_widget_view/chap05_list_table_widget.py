from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, \
    QWidget

from pyqt5_tutorial.chap05_widget_view.chap05_list import MySimpleList
from pyqt5_tutorial.chap05_widget_view.chap05_list_model import MyListWithModel
from pyqt5_tutorial.chap05_widget_view.chap05_table import MySimpleTable
from pyqt5_tutorial.chap05_widget_view.chap05_table02 import MySimpleTable01
from pyqt5_tutorial.chap05_widget_view.chap05_table_advance import MyAdvanceTable
from pyqt5_tutorial.chap05_widget_view.chap05_table_model import MyTableViewModelAdvance
from pyqt5_tutorial.chap05_widget_view.chap05_table_model_advance import MyTableViewModel


class MyListTable(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget & QTableWidget')
        self.setGeometry(0, 0, 1200, 700)
        self.init_ui()

    def init_ui(self):

        layout_list = QHBoxLayout()
        layout_list.addWidget(MySimpleList())
        layout_list.addWidget(MyListWithModel())
        layout_list.addWidget(MySimpleTable())

        # tablewidget & tableView
        layout_table = QHBoxLayout()
        layout_table.addWidget(MySimpleTable01())
        layout_table.addWidget(MyAdvanceTable())
        layout_table.addWidget(MyTableViewModel())
        layout_table.addWidget(MyTableViewModelAdvance())

        # total alyout
        layout = QVBoxLayout()
        layout.addLayout(layout_list)
        layout.addLayout(layout_table)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    win = MyListTable()
    win.show()
    app.exec_()