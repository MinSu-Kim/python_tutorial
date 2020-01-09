for i in range(5):
    print(i, end=" ")
    
print()

r1 = range(5,10)

for i in range(5,10):
    print(i, end=" ")

print()

for i in range(1, 10, 3):
    print(i, end=" ")
print()

for i in range(-10, -100, -30):
    print(i, end=" ")
print()


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i in enumerate(a):
    print(i)
    
# loop의 break와 continue 그리고 else절
# 루프 문은 else 절을 가질 수 있습니다; 루프가 리스트의 소진이나 (for 의 경우) 조건이 거짓이 돼서 (while 의 경우) 종료할 때 실행됩니다. 
# 하지만 루프가 break 문으로 종료할 때는 실행되지 않습니다

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# continue
for num in range(2,10):
    if num % 2 == 0 :
        print("Found an even number", num)
        continue
    print("found a number", num)
