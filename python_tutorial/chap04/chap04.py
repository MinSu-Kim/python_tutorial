#-*- coding:utf-8 -*-

print('if 문')
# x = int(input("Please enter an integer: "))
x = 0
if x < 0 :
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
    
#for 문
print('\nfor 문-01')
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print('\nfor 문-02')   
print(words) 
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)

# for w in words: 를 쓰면, 위의 예는 defenestrate를 반복해서 넣고 또 넣음으로써, 무한한 리스트를 만들려고 시도.
i=0
for w in words:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
    if i==5:
        break
    i=i+1
    
print(words)


        