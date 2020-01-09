from multiprocessing import Pool
import time
import os
import math

# 하나의 프로세스속 함수가 time.sleep(1)으로 인해 잠깐 멈추어도 다른 프로세스에서 돌아가는 함수는 계속 인자를 분배 받아 진행합니다.
# 이 처럼 Pool 을 통해 데이터를 병렬화 해서 함수의 결과를 훨씬더 빠르게 받을수 있습니다.


def f(x):
    print("값", x, "에 대한 작업 Pid = ", os.getpid())
    time.sleep(1)
    return x * x


if __name__ == '__main__':
    p = Pool(3)
    startTime = int(time.time())
    print(p.map(f, range(0, 10)))  # 함수와 인자값을 맵핑하면서 데이터를 분배한다
    endTime = int(time.time())
    print("총 작업 시간", (endTime - startTime))
