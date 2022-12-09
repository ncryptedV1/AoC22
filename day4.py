file = open('in.txt', 'r')


def to_ints(x):
    return [int(y) for y in x.split('-')]


def contained(x, y):
    x1, x2 = to_ints(x)
    y1, y2 = to_ints(y)
    if x1 <= y1 and x2 >= y2:
        return True


def overlap(x, y):
    x1, x2 = to_ints(x)
    y1, y2 = to_ints(y)
    if x1 <= y1 <= x2:
        return True


res = 0
for line in file.readlines():
    a, b = line.split(',')
    if overlap(a, b) or overlap(b, a):
        res += 1
print(res)
