from os.path import expanduser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDirModel, QTableView, QHeaderView, QAbstractItemView

home_directory = expanduser("~")

class DirModel(QDirModel):
    def data(self, index, role):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignVCenter|Qt.AlignRight
        return super(DirModel, self).data(index, role)

    def headerData(self, section, orientation, role):
        if section == 3 and orientation == Qt.Horizontal and role==Qt.DisplayRole:
            return "Modified"
        return super().headerData(section, orientation, role)

app = QApplication([])
model = DirModel()
# view = QTreeView()
view = QTableView()
view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
view.setSelectionBehavior(QAbstractItemView.SelectRows)
view.setWindowTitle("탐색기")
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()
app.exec_()