from python_tutorial.module import fibo

if __name__ == '__main__':
    print('__name__ => ', __name__)
    print('fibo.__name__ => ', fibo.__name__)

    fib = fibo.fib
    fib(200)
    fib(100)
