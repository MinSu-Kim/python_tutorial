from python_tutorial.module.fibo import fib

if __name__ == "__main__":
    import sys
    print('sys.argv : ', sys.argv)
    fib(int(sys.argv[1]))