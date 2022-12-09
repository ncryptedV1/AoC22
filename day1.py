in_file = open('in.txt', 'r')
cur_sum = 0
sums = []
for line in in_file.readlines():
    if line.strip() == '':
        sums.append(cur_sum)
        cur_sum = 0
    else:
        cur_sum += int(line)
sums.append(cur_sum)
sums.sort(reverse=True)
print(sum(sums[:3]))
