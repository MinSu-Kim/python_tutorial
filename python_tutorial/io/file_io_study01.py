f = open('workfile.txt', 'r', encoding='utf-8')
read_data = f.read()
print(read_data)
f.close()
print('f.closed : ', f.closed)

print()
with open('workfile.txt', 'r') as f:
    read_data = f.read()
    print('f.encoding : ', f.encoding)
    print(read_data)

print('f.closed : ', f.closed)

f.read()
