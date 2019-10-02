import math

print("원주율을 소수점 이하 세 자리로 반올림")
print(f'The value of pi is approximately {math.pi:.3f}.')
print()
print("':' 뒤에 정수를 전달하면 해당 필드의 최소 문자 폭")
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print("""
수정자를 사용하면 포맷되기 전에 값을 변환할 수 있습니다. 
'!a'는 ascii()를, 
'!s'는 str()을, 
'!r'는 repr()을 적용""")
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')