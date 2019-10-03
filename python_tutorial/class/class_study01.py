class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print('x.r : {}, x.i :{}'.format(x.r, x.i))

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)

print(dir(x))
del x.counter
print(dir(x))
