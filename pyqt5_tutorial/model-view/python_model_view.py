from os.path import expanduser

from PyQt5.QtWidgets import QApplication, QDirModel, QTreeView, QTableView, QHeaderView

home_directory = expanduser("~")

app = QApplication([])
model = QDirModel()
# view = QTreeView()
view = QTableView()
view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
view.setWindowTitle("탐색기")
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()
app.exec_()