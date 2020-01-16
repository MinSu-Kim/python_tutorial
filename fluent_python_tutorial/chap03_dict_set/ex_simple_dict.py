a = dict(one=1, two=2, three=3)
print("dict(one=1, two=2, three=3)")
print(type(a), a, sep='\n', end='\n\n')

b = {'one': 1, 'two': 2, 'three': 3}
print("{'one': 1, 'two': 2, 'three': 3}")
print(type(b), b, sep='\n', end='\n\n')

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print("dict(zip(['one', 'two', 'three'], [1, 2, 3]))")
print(type(c), c, sep='\n', end='\n\n')

d = dict([('two', 2), ('one', 1), ('three', 3)])
print("dict([('two', 2), ('one', 1), ('three', 3)])")
print(type(d), d, sep='\n', end='\n\n')

e = dict({'one': 1, 'two': 2, 'three': 3})
print("dict({'one': 1, 'two': 2, 'three': 3})")
print(type(e), e, sep='\n', end='\n\n')

print(a==b==c==d==e)