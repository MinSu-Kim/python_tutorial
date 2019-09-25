from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QHBoxLayout, QListWidget, QMainWindow, QApplication, \
    QWidget, QLineEdit, QPushButton, QSpinBox


class MyListTable(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget & QTableWidget')
        self.setGeometry(0, 0, 600, 400)
        self.init_ui()

    def init_ui(self):
        group_list = self.create_list()

        layout = QVBoxLayout()
        layout.addWidget(group_list)
        layout.addStretch(1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def create_list(self):
        group_list = QGroupBox('QListWidget')

        list = QListWidget()

        layout_add = QHBoxLayout()
        line_add_edit = QLineEdit('Add Item')
        add_btn = QPushButton('add')
        layout_add.addWidget(line_add_edit)
        layout_add.addWidget(add_btn)

        layout_insert = QHBoxLayout()
        layout_btns = QHBoxLayout()
        line_insert_position_edit = QLineEdit('Insert Item')
        spinbox_pos = QSpinBox()
        spinbox_pos.setRange(0, list.count())   # list항목이 추가되면 max도 변경되도록 추
        spinbox_pos.setMaximum(30)
        insert_btn = QPushButton('Insert')
        layout_insert.addWidget(line_insert_position_edit)
        layout_insert.addWidget(spinbox_pos)
        layout_insert.addWidget(insert_btn)


        layout = QVBoxLayout()
        layout.addWidget(list)
        layout.addLayout(layout_add)
        layout.addLayout(layout_insert)
        layout.addLayout(layout_btns)

        group_list.setLayout(layout)
        return group_list


if __name__ == "__main__":
    app = QApplication([])
    win = MyListTable()
    win.show()
    app.exec_()