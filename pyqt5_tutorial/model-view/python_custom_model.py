import typing

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel, QAbstractTableModel, QModelIndex, Qt, QVariant

headers = ["Scientist name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-13-14", "Relativity"),
        ("Darwin", "1809-0212", "Evolution")]


class TableModel(QAbstractTableModel):
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return headers[section]

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.TextAlignmentRole:
            if 0 == index.column() :
                return Qt.AlignVCenter | Qt.AlignCenter
            if 1 == index.column() :
                return Qt.AlignVCenter | Qt.AlignLeft
            if 2 == index.column() :
                return Qt.AlignVCenter | Qt.AlignTrailing
        if role != Qt.DisplayRole:
            return QVariant()

        return rows[index.row()][index.column()]

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(headers)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(rows)


app = QApplication([])
model = TableModel()
view = QTableView()
view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
view.resize(400, 300)
view.setWindowTitle("QStringListModel & QListView")
view.setModel(model)
view.show()
app.exec_()