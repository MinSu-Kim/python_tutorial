import json

from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

tick = QtGui.QImage('../../icons/tick.png')


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []  # todos = [( False ,  'an item' ),  ( False ,  'another item' )] 없을 경우 빈 할일 목록

    def data(self, index, role):
        if role == Qt.DisplayRole:               # 텍스트 형식으로 렌더링 할 키 데이터(QString)
            _, text = self.todos[index.row()]
            return text
        if role == Qt.DecorationRole:            # 아이콘 형태로 장식으로 렌더링 할 데이터 (QColor , QIcon, QPixmap)
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('mainwindow.ui', self)

        self.setWindowIcon(QIcon('../../data/web.png'))
        self.model = TodoModel(todos=[(False, 'my first todo'), (True, 'my second todo')])
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        text = self.todoEdit.text()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            # 데이터의 모양이 변경되었음을 뷰에 알리기 위해 layoutChange 모델 신호를 보내고 layoutChang신호를 받은
            # QListView는 업데이트 됨  위의 줄을 생략해도 작업 내용이 추가되지만 QListView는 업데이트되지 않는다.
            self.todoEdit.setText("")
            self.save()

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()   # 선택 초기화
            self.save()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index) # 선택된 요소만 새로고침
            self.todoView.clearSelection()
            self.save()

    def load(self):
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.db', 'w') as f:
            data = json.dump(self.model.todos, f)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
