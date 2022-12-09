file = open('in.txt', 'r')

knot_count = 10
knot_pos = [(0, 0)] * knot_count
t_vis = set()
t_vis.add(knot_pos[-1])


def move_step(pos, direction):
    x, y = pos
    switch = {
        'L': (x - 1, y),
        'R': (x + 1, y),
        'U': (x, y + 1),
        'D': (x, y - 1)
    }
    return switch[direction]


def print_pos():
    xs = [x[0] for x in knot_pos]
    ys = [x[1] for x in knot_pos]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    h = max_y - min_y + 1
    w = max_x - min_x + 1
    pos = [['.'] * w for _ in range(h)]
    for idx, knot in enumerate(knot_pos):
        x, y = knot
        pos[y-min_y][x-min_x] = str(idx)
    for pos_line in pos:
        print(''.join(pos_line))
    print()


for line in file.readlines():
    direction, dist = line.split(' ')
    dist = int(dist)
    # iterate over every step for head
    for _ in range(dist):
        # move head
        knot_pos[0] = move_step(knot_pos[0], direction)

        for knot_idx in range(1, knot_count):
            cur_pos = knot_pos[knot_idx]
            cur_x, cur_y = cur_pos
            prev_pos = knot_pos[knot_idx - 1]
            prev_x, prev_y = prev_pos

            # calc dist to prev knot
            dx = prev_x - cur_x
            dy = prev_y - cur_y

            # conclude tail steps
            h_dir = 'R' if dx > 0 else 'L'
            v_dir = 'U' if dy > 0 else 'D'
            next_pos = cur_pos
            if abs(dx) > 1:
                # correct horizontally
                next_pos = move_step(next_pos, h_dir)
                if dy != 0:
                    next_pos = move_step(next_pos, v_dir)
            elif abs(dy) > 1:
                # correct vertically
                next_pos = move_step(next_pos, v_dir)
                if dx != 0:
                    next_pos = move_step(next_pos, h_dir)
            knot_pos[knot_idx] = next_pos

            if knot_idx == knot_count - 1:
                t_vis.add(next_pos)
    # print_pos()

print(len(t_vis))
