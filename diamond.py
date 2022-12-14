side = 8
height = list(range(side)) + list(reversed(range(side - 1)))
pattern = '{: <{space}}{:*<{val}}'
for x in height:
    a = side - x - 1
    b = x * 2 + 1
    print(pattern.format('', '', space=a, val=b))

n=5
for i in range(n):
    for j in range(i+1):
        print('* ', end=' ')
    print()
