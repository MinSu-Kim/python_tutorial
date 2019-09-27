from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem


class MySimpleTable(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('Simple Table Widget')
        self.init_ui()

    def init_ui(self):
        self.tableWidget = QTableWidget()

        # set row count
        self.tableWidget.setRowCount(4)

        # set column count
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))

        self.tableWidget.doubleClicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)

    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())