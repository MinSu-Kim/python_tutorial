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
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)


        