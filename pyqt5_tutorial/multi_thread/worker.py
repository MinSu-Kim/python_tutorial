# 추가 모듈
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
import time

# 백그라운드에서 돌아갈 함수 class
class Worker(QObject):
    # 시그널 객체를 하나 생성합니다.
    sig_numbers = pyqtSignal(int)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    @pyqtSlot()           # 버튼이 클릭시 시그널을 받아들이는 슬롯을 하나 마련합니다.
    def startWork(self):
        _cnt = 0
        while _cnt < 10:
            _cnt += 1
            self.sig_numbers.emit(_cnt) # pyqtSignal 에 숫자데이터를 넣어 보낸다
            print(_cnt)                 # consol에서 어떻게 진행 되는지 보기 위해서 넣어준다
            time.sleep(1)