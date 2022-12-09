file = open('in.txt', 'r')
lines = file.readlines()
res = 0
for group_idx in range(0, len(lines), 3):
    used = set([x for x in lines[group_idx]])
    matches_sec = [x for x in lines[group_idx+1] if x in used]
    badge = [x for x in lines[group_idx+2] if x in matches_sec][0]
    prio = ord(badge)
    if prio < 91:
        res += prio - 65 + 27
    else:
        res += prio - 97 + 1
print(res)
