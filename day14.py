file = open('in.txt', 'r')
lines = [line.strip() for line in file.readlines()]

sand = (500, 0)

paths = [line.split(' -> ') for line in lines]
for idx, path in enumerate(paths):
    path = [coord.split(',') for coord in path]
    path = [tuple(int(part) for part in coord) for coord in path]
    paths[idx] = path

# generate state map
apply_to_part = lambda fct, part: fct(fct(fct(coord[part] for coord in path) for path in paths), sand[part])
min_x = apply_to_part(min, 0) - 300
max_x = apply_to_part(max, 0) + 300
max_y = apply_to_part(max, 1) + 2
width = max_x - min_x + 1
height = max_y + 1
# 0-air, 1-rock, 2-sand
state = [[0] * width for _ in range(height)]

# norm everything to 0-based
norm_coord = lambda coord: (coord[0] - min_x, coord[1])
paths = [[norm_coord(coord) for coord in path] for path in paths]
sand = norm_coord(sand)

# add bottom floor as path
paths.append([(0, height - 1), (width - 1, height - 1)])

# draw paths
for path in paths:
    prev_coord = path[0]
    for coord in path[1:]:
        dx = coord[0] - prev_coord[0]
        dy = coord[1] - prev_coord[1]
        dir_y = dy != 0
        max_d = dx if dx != 0 else dy
        sign = -1 if max_d < 0 else 1
        for step in range(abs(max_d) + 1):
            x = prev_coord[0] + (sign * step if not dir_y else 0)
            y = prev_coord[1] + (sign * step if dir_y else 0)
            state[y][x] = 1
        prev_coord = coord

sand_drawn = 0

# start simulation
sand_in_bounds = True
while sand_in_bounds:
    cur_sand_pos = sand
    pos_changed = True
    sand_drawn += 1
    while pos_changed:
        to_check = [(0, 1), (-1, 1), (1, 1)]
        # as long as sand isn't lying still -> animate
        pos_changed = False
        for check_dif in to_check:
            dx, dy = check_dif
            check_pos = (cur_sand_pos[0] + dx, cur_sand_pos[1] + dy)
            check_x, check_y = check_pos
            if state[check_y][check_x] == 0:
                state[check_y][check_x] = 2
                state[cur_sand_pos[1]][cur_sand_pos[0]] = 0
                cur_sand_pos = check_pos
                pos_changed = True
                break
        # check no movement occuring
        if cur_sand_pos == sand:
            sand_in_bounds = False
            break
# remove last sand pixel that fell out of world
# sand_drawn -= 1

# print map
for y in state:
    line = ''
    for x in y:
        line += str(x)
    print(line)

print(sand_drawn)
