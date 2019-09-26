from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QVariant


class DataModel(QtCore.QAbstractListModel):
    def __init__(self, data=None):
        super().__init__()
        self.data = data or []  # todos = [( False ,  'an item' ),  ( False ,  'another item' )] 없을 경우 빈 할일 목록

    def data(self, index, role=None):
        if role == Qt.DisplayRole:  # 텍스트 형식으로 렌더링 할 키 데이터(QString)
            text = self.data[index.row()]
            return text
        if role == Qt.DecorationRole:  # 아이콘 형태로 장식으로 렌더링 할 데이터 (QColor , QIcon, QPixmap)
            return QVariant()

    def rowCount(self, index=None):
        return len(self.data)


