from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel

app = QApplication([])
model = QStringListModel(["An element", "Another element", "Yay! Another one."])
view = QListView()
view.resize(400, 300)
view.setWindowTitle("QStringListModel & QListView")
view.setModel(model)
view.show()
app.exec_()