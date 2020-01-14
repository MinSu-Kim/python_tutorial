with open('workfile.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end= '')

print('\n')
with open('workfile.txt', 'r', encoding='utf-8') as f:
   l = list(f)
   print(l)

print()
with open('workfile.txt', 'r', encoding='utf-8') as f:
   l = f.readlines()
   print(l)