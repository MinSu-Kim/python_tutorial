import functools

from fluent_python_tutorial.chap07_decoration.ex7_5_simple_decorator import clock

@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


@functools.lru_cache()
@clock
def fibonacci2(n):
    if n<2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)


if __name__=="__main__" :
    print(fibonacci(6))
    print()
    print(fibonacci2(6))