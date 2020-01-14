colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

print()

tshirts = [(c, s) for c in colors for s in sizes]
for c, s in tshirts:
    # print('{} {}'.format(tshirt[0], tshirt[1]))
    print('%s %s' % (c, s))