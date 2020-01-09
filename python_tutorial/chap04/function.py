def gugudan(n):
    """Gugudan """
    for i in range(1,10):
        print(n , "*", i, " = ", n * i)
        

gugudan(3)

g = gugudan
for dan in range(2,10):
    g(dan)
    

def gugudan():
    for dan in range(2, 10):
        for i in range(1,10):
            print("{0} * {1} = {2}".format(dan, i, dan*i))

gugudan()

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('정말 끝내길 원하세요')


# 기본값은 함수 정의 시점에 정의되고 있는 스코프에서 구해집니다, 그래서
i = 5
def f(arg=i):
    print(arg)

i = 6
f()
# 5를 출력함

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


print(list(range(3, 6)))            # normal call with separate arguments

args = [3, 6]
print(list(range(*args)))            # call with arguments unpacked from a list
