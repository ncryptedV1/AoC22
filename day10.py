file = open('in.txt', 'r')

cycle = 0
reg_val = 1
last_sync_step = -1

width = 40
height = 6
screen = [['.'] * width for _ in range(height)]
# res = 0

for line in file.readlines():
    line = line.strip()
    if line == 'noop':
        cur_cycles = 1
        v = 0
    elif line.startswith('addx'):
        cur_cycles = 2
        v = int(line.split(' ')[1])

    for _ in range(cur_cycles):
        x = cycle % width
        y = cycle // width
        if reg_val - 1 <= x <= reg_val + 1:
            screen[y][x] = '#'
        cycle += 1

    # sync_step = (cycle - 20) // 40
    # if sync_step > last_sync_step:
    #     res += x * (sync_step * 40 + 20)
    #     last_sync_step = sync_step
    reg_val += v

# print(res)
for line in screen:
    print(''.join(line))
