import timeit


def non_ascii(c):
    return c > 127


symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(codes)
codes = [ord(s) for s in symbols if non_ascii(ord(s))]
print(codes)
codes = list(filter(lambda c: c > 127, map(ord, symbols)))
print(codes)
codes = list(filter(non_ascii, map(ord, symbols)))
print(codes)

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')


