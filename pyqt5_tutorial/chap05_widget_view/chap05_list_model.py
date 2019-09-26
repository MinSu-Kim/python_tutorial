from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QApplication, \
    QLineEdit, QPushButton, QSpinBox, QListView

from pyqt5_tutorial.chap05_widget_view.ListModel import DataModel


class QStringModel(object):
    pass


class MyListWithModel(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('MyListWithModel')
        self.init_ui()

    def init_ui(self):
        self.listview = QListView()
        self.model = DataModel(data=[('my first todo'), ('my second todo')])
        self.listview.setModel(self.model)
        self.listview.setSelectionMode(QListView.MultiSelection)

        # add Layout
        layout_add = QHBoxLayout()
        self.line_add_edit = QLineEdit('Add Item')
        add_btn = QPushButton('add')
        layout_add.addWidget(self.line_add_edit)
        layout_add.addWidget(add_btn)

        # insert to position layout
        layout_insert = QHBoxLayout()
        self.line_insert_position_edit = QLineEdit('Insert Item')
        self.spinbox_pos = QSpinBox()

        self.spinbox_pos.setRange(0, self.model.rowCount())  # list항목이 추가되면 max도 변경되도록 추가할 것
        insert_btn = QPushButton('Insert')
        layout_insert.addWidget(self.line_insert_position_edit)
        layout_insert.addWidget(self.spinbox_pos)
        layout_insert.addWidget(insert_btn)

        print_btn = QPushButton('Print')
        print_multi_btn = QPushButton('Print Multi')
        remove_btn = QPushButton('Current Item Remove')
        clear_btn = QPushButton('Clear')

        # connect
        add_btn.clicked.connect(self.add_item)
        insert_btn.clicked.connect(self.insert_pos_item)

        print_btn.clicked.connect(lambda: print(self.listview.selectedIndexes()[0]))
        print_multi_btn.clicked.connect(self.print_multi_items)
        remove_btn.clicked.connect(self.remove_current_item)
        clear_btn.clicked.connect(self.clear_listview)

        layout_btns = QHBoxLayout()
        layout_btns.addWidget(print_btn)
        layout_btns.addWidget(print_multi_btn)
        layout_btns.addWidget(remove_btn)
        layout_btns.addWidget(clear_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.listview)
        layout.addLayout(layout_add)
        layout.addLayout(layout_insert)
        layout.addLayout(layout_btns)

        self.setLayout(layout)

    def add_item(self):
        item = self.line_add_edit.text()

        if item:
            self.model.data.append(item)
            self.model.layoutChanged.emit()

    def insert_pos_item(self):
        item = self.line_insert_position_edit.text()
        row = self.spinbox_pos.value()
        if item:
            self.model.data.insert(row, item)
            self.spinbox_pos.setMaximum(len(self.model.data))
            self.model.layoutChanged.emit()

    def remove_current_item(self):
        indexes = self.listview.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.data[index.row()]
            self.model.layoutChanged.emit()
            self.listview.clearSelection()

    def print_multi_items(self):
        indexes = self.listview.selectedIndexes()
        print(type(indexes))
        for i in indexes:
            print(self.model.data[i.row()])


    def clear_listview(self):
        self.model.data = []
        self.model.layoutChanged.emit()


if __name__ == "__main__":
    app = QApplication([])
    win = MyListWithModel()
    win.show()
    app.exec_()