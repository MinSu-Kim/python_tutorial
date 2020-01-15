# 리스트의 리스트 생성하기

board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)
print()


# 세개의 행이 동일한 객체를 참조
weird = [['_'] * 3] * 3
print(weird)
weird[1][2] = 'X'
print(weird)
print()

row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)

print()
print(board)
board[1][2] = 'X'
print(board)


# listcomprehension 적용방식
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print()
print(board)
board[1][2] = 'X'
print(board)



# 시퀀스 복합할당
l = [1, 2, 3]
print(l, id(l))
l *= 2
print(l, id(l))
print()

t = (1, 2, 3)
print(t, id(t))
t *= 2
print(t, id(t))

#
print()
t1 = (1, 2, [30, 40])
print(t1, id(t1))
# t1[2] += [50, 60]
# print(t1)


#s[a] += b 동작순서
import dis
print("dis.dis('s[a] += b') ==> ", dis.dis('s[a] += b'))


