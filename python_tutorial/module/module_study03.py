import sys

from python_tutorial.module import fibo

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print('type(dir(fibo)) : ', type(dir(fibo)), end='\n')
    print(dir(fibo), end='\n')
    print('dir(sys)', dir(sys), end='\n')

    for d in dir():
        print(d)