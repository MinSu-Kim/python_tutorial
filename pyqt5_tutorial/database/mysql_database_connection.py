from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QTableView, QApplication
import sys


def dbcon():
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('ncs_coffee')
    db.setUserName('user_ncs_coffee')
    db.setPassword('rootroot')
    ok = db.open()
    if not ok: print(db.lastError().text())
    # else: print("connected")
    query = QSqlQuery(db)
    query.exec_('"SELECT code, name FROM product"')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dbcon()