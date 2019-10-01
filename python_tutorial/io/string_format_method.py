# str.format() 메서드의 기본적인 사용법
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# 중괄호와 그 안에 있는 문자들 (포맷 필드)은 str.format() 메서드로 전달된 객체들로 치환
# 중괄호 안의 숫자는 str.format()메서드로 전달된 객체들의 위치를 가리키는데 사용
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# str.format() 메서드에 키워드 인자가 사용되면, 그 값들은 인자의 이름을 사용해서 지정할 수 있음
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# 위치와 키워드 인자를 자유롭게 조합할 수 있음
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# 딕셔너리를 넘기고 키를 액세스하는데 대괄호 '[]' 를 사용
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# '**' 표기법을 사용해서 table을 키워드 인자로 전달해도 같은 결과
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

