import os

from multiprocessing import Process


# Process 는 Pool 과는 다르게 인수를 퐁당퐁당 건너서 제공하는 것은 아니고 그저 하나의 프로세스를
# 하나의 함수에 적당한 인자값을 할당 해주고(없어도 됩니다) 더이상 신경을 안씁니다.  예제를 보겠습니다.

def doubler(number):
    # A doubling function that can be used by a process

    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
