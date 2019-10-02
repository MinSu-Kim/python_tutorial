def bool_return():
    try:
        return True
    finally:
        return False


def divide(x, y):
    print('divide({}, {})'.format(x, y), end='\n')
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


if __name__ == "__main__":
    # print('bool_return() : ', bool_return())
    # divide(2, 1)
    # divide(2, 0)
    divide("2", "1")
    # try:
    #     divide("2", "1")
    # except BaseException as e:
    #     print('BaseException => ', e)
