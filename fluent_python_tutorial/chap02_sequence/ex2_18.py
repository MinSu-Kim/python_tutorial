import bisect
import random

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


g = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(g)

SIZE =7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print("%2d ->" % new_item, my_list)

