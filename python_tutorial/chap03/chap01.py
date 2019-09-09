#-*- coding:utf-8 -*-

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1

while a < 10:
    print(a)
    a, b = b, a+b
    
print('>>>>>>>>')

a, b = 0, 1
while a < 1000:
    print(a, end=', ')
    a, b = b, a+b
   
print() 
print('>>>>>>>>')

print(2+2)

# 나눗셈 (/) 은 항상 float를 돌려줍니다. 정수 나눗셈 으로 (소수부 없이) 정수 결과를 얻으려면 
# '//' 연산자를 사용
print(17/3)
print(17//3)


squares = [1, 4, 9, 16, 25]
print('squares', squares)
print('squares[0] = ', squares[0], ' squares[3]', squares[3])
print('squares[-1] = ', squares[-1], ' squares[-3]', squares[-3])


    