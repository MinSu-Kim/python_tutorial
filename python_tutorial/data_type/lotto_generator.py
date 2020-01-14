import random

# 5천원치 로또번호 생성
lotto_5 = []
print(lotto_5.__len__())
random.seed(1234)

while lotto_5.__len__() != 5:
    set1 = set()
    while set1.__len__() != 6:
        set1.add(random.randint(1, 45))
    lotto = list(set1)
    lotto.sort()
    lotto_5.append(lotto)

print(lotto_5)


# 당첨번호 확인

def lotto_rank(x):
    lotto_rnk = {1: '꽝',
                 2: '꽝',
                 3: '3개일치',
                 4: '4개일치',
                 5: '5개일치',
                 6: '신'}
    return lotto_rnk.get(x)


# 1등 당첨번호
fst_lotto = {6, 7, 16, 23, 43, 45}

for lst in lotto_5:
    set1 = set(lst)
    cnt_num = set1.intersection(fst_lotto)
    print(cnt_num.__len__(), cnt_num)
    print(lotto_rank(cnt_num.__len__()))
