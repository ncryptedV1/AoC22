file = open('in.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]
height = len(lines)
width = len(lines[0])


def get_height(x, y):
    return int(lines[y][x])


vis_map = [[0 for _ in range(width)] for _ in range(height)]


def update_vis(y_seq, x_seq, switch_xy):
    for y in y_seq:
        last_height = -1
        for x in x_seq:
            norm_x, norm_y = x, y
            if switch_xy:
                norm_x, norm_y = norm_y, norm_x
            cur_height = get_height(norm_x, norm_y)
            if cur_height <= last_height:
                continue
            vis_map[norm_y][norm_x] = 1
            last_height = cur_height


def get_view_dist(y_seq, x_seq, init_height):
    view_dist = 0
    for y, x in list(zip(y_seq, x_seq)):
        view_dist += 1
        if get_height(x, y) >= init_height:
            return view_dist
    return view_dist


def calc_score(y, x):
    h = get_height(x, y)
    # to left
    l = get_view_dist([y] * x, range(x - 1, -1, -1), h)
    # to right
    r = get_view_dist([y] * (width - x - 1), range(x + 1, width), h)
    # to top
    t = get_view_dist(range(y - 1, -1, -1), [x] * y, h)
    # to bottom
    b = get_view_dist(range(y + 1, height), [x] * (height - y - 1), h)
    return l * r * t * b


max_score = 0
for y in range(height):
    for x in range(width):
        max_score = max(max_score, calc_score(y, x))

print(max_score)



