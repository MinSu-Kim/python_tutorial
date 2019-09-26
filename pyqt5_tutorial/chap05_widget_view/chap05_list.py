from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QHBoxLayout, QListWidget, QMainWindow, QApplication, \
    QWidget, QLineEdit, QPushButton, QSpinBox


class MySimpleList(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('SimpleList')
        self.init_ui()

    def init_ui(self):
        self.list = QListWidget()
        self.list.setSelectionMode(QListWidget.MultiSelection)

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
        print(self.list.count())
        self.spinbox_pos.setRange(0, self.list.count())  # list항목이 추가되면 max도 변경되도록 추가할 것
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

        print_btn.clicked.connect(lambda: print(self.list.currentItem().text()))
        print_multi_btn.clicked.connect(self.print_multi_items)
        remove_btn.clicked.connect(self.remove_current_item)
        clear_btn.clicked.connect(lambda: self.list.clear())

        layout_btns = QHBoxLayout()
        layout_btns.addWidget(print_btn)
        layout_btns.addWidget(print_multi_btn)
        layout_btns.addWidget(remove_btn)
        layout_btns.addWidget(clear_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addLayout(layout_add)
        layout.addLayout(layout_insert)
        layout.addLayout(layout_btns)

        self.setLayout(layout)

    def add_item(self):
        print('add_item')
        self.list.addItem(self.line_add_edit.text())
        self.spinbox_pos.setMaximum(self.list.count())

    def insert_pos_item(self):
        item = self.line_insert_position_edit.text()
        row = self.spinbox_pos.value()
        self.list.insertItem(row, item)
        self.spinbox_pos.setMaximum(self.list.count())

    def print_multi_items(self):
        for i in self.list.selectedItems():
            print(i.text())

    def remove_current_item(self):
        selectedRow = self.list.currentRow()
        removeItem = self.list.takeItem(selectedRow)
        print(removeItem.text(), ' 삭제')


if __name__ == "__main__":
    app = QApplication([])
    win = MySimpleList()
    win.show()
    app.exec_()