in_file = open('in.txt', 'r')

# Rock -> Scissors -> Paper -> Rock
# x wins against y
win_dict = {
    1: 3,
    2: 1,
    3: 2
}
# x loses against y
lose_dict = {
    1: 2,
    2: 3,
    3: 1
}


def conv_to_int(x):
    # A, X1 - Rock
    # B, Y2 - Paper
    # C, Z3 - Scissors
    if x == 'A' or x == 'X':
        return 1
    elif x == 'B' or x == 'Y':
        return 2
    elif x == 'C' or x == 'Z':
        return 3


def calc_outcome(x, y):
    # 0 - y loses
    # 3 - draw
    # 6 - y wins
    if x == y:
        return 3
    elif lose_dict[x] == y:
        return 6
    elif win_dict[x] == y:
        return 0


def shape_to_play(x, y):
    # x - shape of opponent
    # y - desired outcome
    # X - lose, Y - draw, Z - win
    if y == 'Y':
        return x
    elif y == 'X':
        return win_dict[x]
    elif y == 'Z':
        return lose_dict[x]


res = 0
for line in in_file.readlines():
    first, outcome = line.strip().split(" ")
    first = conv_to_int(first)
    second = shape_to_play(first, outcome)
    res += second
    res += 6 if outcome == 'Z' else 3 if outcome == 'Y' else 0
print(res)


