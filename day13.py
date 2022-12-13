import ast
from functools import cmp_to_key

file = open('in.txt', 'r')
lines = [line.strip() for line in file.readlines()]


# -1 lt, 0 eq, 1 gt
def compare_int(a, b):
    return -1 if a < b else 0 if a == b else 1


# -1 lt, 0 eq, 1 gt
def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return compare_int(a, b)
    else:
        if not isinstance(a, list):
            a = [a]
        elif not isinstance(b, list):
            b = [b]
        for idx in range(len(a)):
            # length of a has surpassed b -> wrong order
            if idx == len(b):
                return 1
            comp_res = compare(a[idx], b[idx])
            if comp_res != 0:
                return comp_res
        # length of b has surpassed a -> right order
        if len(b) > len(a):
            return -1
        else:
            return 0


packets = [ast.literal_eval(line) for line in lines if line]
packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
