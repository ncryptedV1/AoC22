file = open('in.txt', 'r')

cur_pos = []
fs = {}


def get_fs_at_path(path):
    cur = fs
    for element in path:
        if element not in cur:
            cur[element] = {}
        cur = cur.get(element)
    return cur


for line in file.readlines():
    line = line.strip()
    if line.startswith('$'):
        line = line[2:]
        if line.startswith('cd'):
            target = line[3:]
            if target == '/':
                cur_pos.append('/')
            elif target == '..':
                cur_pos.pop()
            else:
                cur_pos.append(target)
        elif line.startswith('ls'):
            pass
    else:
        # ls output
        if line.startswith('dir'):
            name = line[4:]
            get_fs_at_path(cur_pos)[name] = {}
        else:
            file_size = int(line.split(' ')[0])
            name = line.split(' ')[1]
            get_fs_at_path(cur_pos)[name] = {'_size_': file_size}


res = 0
dir_sizes = []


def traverse(parent):
    global res
    total_size = 0
    for key, value in parent.items():
        # file -> contains just _size_ key, value pair
        if len(value.items()) == 1 and list(value.keys())[0] == '_size_':
            total_size += value['_size_']
        else:
            total_size += traverse(value)
    parent['_size_'] = total_size
    dir_sizes.append(total_size)
    return total_size


traverse(fs['/'])
used_space = fs['/']['_size_']
free_space = 70_000_000 - used_space
req_space = 30_000_000 - free_space
dir_sizes.sort()
res = next(x for x in dir_sizes if x >= req_space)
print(res)
