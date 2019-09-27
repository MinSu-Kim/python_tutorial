from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt


class MyTableModel(QAbstractTableModel):
    def __init__(self, data=None, headerData=None):
        super().__init__()
        self.data = data or []
        self.header = headerData

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.data[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()
