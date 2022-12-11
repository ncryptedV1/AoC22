from tqdm import tqdm

file = open('in.txt', 'r')
lines = file.readlines()

op_dict = {
    '+': 0,
    '*': 1
}

monkey_meta = []
# idx for items_list
monkey_items = []
# 0: base worry
# 1-n: tuple (op, op_nr)
items_list = []

for lines_idx in range(0, len(lines), 7):
    monkey_lines = [line.strip() for line in lines[lines_idx:lines_idx + 7]]
    monkey_idx = int(monkey_lines[0].split(' ')[1][:-1])
    items = [int(item) for item in monkey_lines[1][16:].split(', ')]

    op = op_dict[monkey_lines[2].split(' ')[-2]]
    op_nr = monkey_lines[2].split(' ')[-1]
    op_nr = -1 if op_nr == 'old' else int(op_nr)
    test_nr = int(monkey_lines[3].split(' ')[-1])
    true_monkey_idx = int(monkey_lines[4].split(' ')[-1])
    false_monkey_idx = int(monkey_lines[5].split(' ')[-1])

    base_idx = len(items_list)
    items_list.extend([[item] for item in items])
    monkey_items.append([base_idx + idx for idx in range(len(items))])
    monkey_meta.append((op, op_nr, test_nr, true_monkey_idx, false_monkey_idx))

monkey_count = len(monkey_items)
inspect_count = [0 for _ in range(monkey_count)]
rounds = 10_000
# items idx: dict -> mod_nr: (op_idx, res)
mod_cache = {idx: {} for idx in range(len(items_list))}


def apply_op(nr, op, op_nr):
    if op_nr == -1:
        op_nr = nr
    if op == 0:
        return nr + op_nr
    elif op == 1:
        return nr * op_nr


for round_idx in tqdm(range(rounds)):
    for monkey_idx in range(monkey_count):
        inspect_count[monkey_idx] += len(monkey_items[monkey_idx])
        for item_idx in monkey_items[monkey_idx]:
            op, op_nr, test_nr, true_idx, false_idx = monkey_meta[monkey_idx]
            item = items_list[item_idx]
            item.append((op, op_nr))
            # load worry from mod cache
            if test_nr not in mod_cache[item_idx]:
                # init default to mod cache
                mod_cache[item_idx][test_nr] = (0, item[0])
            mod_cache_op_idx, worry = mod_cache[item_idx][test_nr]
            # iterate over operation steps
            for ops in item[mod_cache_op_idx + 1:]:
                worry = apply_op(worry, ops[0], ops[1]) % test_nr
            # save to cache
            mod_cache[item_idx][test_nr] = (len(item) - 1, worry)
            if worry == 0:
                monkey_items[true_idx].append(item_idx)
            else:
                monkey_items[false_idx].append(item_idx)
        monkey_items[monkey_idx].clear()

inspect_count.sort(reverse=True)
print(inspect_count[0] * inspect_count[1])
