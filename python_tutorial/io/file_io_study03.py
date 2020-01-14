with open('write_test.txt', 'w', encoding='utf-8') as f:
    cnt = f.write('This is a test\n')
    value = ('the answer', 42)
    cnt += f.write(str(value))
    print('출력된 문자들의 개수 : ', cnt)

with open('write_test.txt', 'r', encoding='utf-8') as f:
    for line in list(f):
        print(line)
