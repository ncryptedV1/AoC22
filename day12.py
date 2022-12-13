from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Any

file = open('in.txt', 'r')
lines = [line.strip() for line in file.readlines()]

height = len(lines)
width = len(lines[0])

height_map = [-1 for _ in range(height * width)]
end = None


def to_norm_coord(x, y):
    return y * width + x


# init height map
for y in range(height):
    for x in range(width):
        char = lines[y][x]
        norm_coord = to_norm_coord(x, y)
        if char == 'S':
            height_map[norm_coord] = 0
        elif char == 'E':
            end = norm_coord
            height_map[norm_coord] = 25
        else:
            height_map[norm_coord] = ord(char) - 97

# create adjacency list
adj_list = [[] for _ in range(height * width)]
for y in range(height):
    for x in range(width):
        norm_coord = to_norm_coord(x, y)
        neighbors = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        neighbors = [to_norm_coord(x, y) for x, y in neighbors if 0 <= x < width and 0 <= y < height]
        for neighbor in neighbors:
            if height_map[neighbor] <= height_map[norm_coord] + 1:
                adj_list[norm_coord].append(neighbor)

# init start vertices
start_vertices = [idx for idx in range(width * height) if height_map[idx] == 0]

# calc min dist to end for every start vertex and save lowest of all
min_end_dist = float('inf')


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


for start in start_vertices:
    # dijkstra
    dist = [float('inf') for _ in range(height * width)]
    dist[start] = 0
    queue = PriorityQueue()
    queue.put(PrioritizedItem(dist[start], start))

    while not queue.empty():
        item = queue.get()
        cur_dist = item.priority
        vertex = item.item
        if cur_dist > dist[vertex]:
            continue
        for neighbor in adj_list[vertex]:
            if cur_dist + 1 < dist[neighbor]:
                dist[neighbor] = cur_dist + 1
                queue.put(PrioritizedItem(cur_dist + 1, neighbor))
    min_end_dist = min(min_end_dist, dist[end])

print(min_end_dist)
