from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication

from pyqt5_tutorial.layout.boxlayout import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.South)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()