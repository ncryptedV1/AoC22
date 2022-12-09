file = open('in.txt', 'r')
lines = file.readlines()
stack_count = 9
max_stack_size = 8

stacks = [[] for _ in range(stack_count)]

# read stacks
for stack_line in lines[:max_stack_size]:
    for stack_idx in range(stack_count):
        letter_idx = 1 + stack_idx * 4
        letter = stack_line[letter_idx]
        if letter.strip() != '':
            stacks[stack_idx].append(letter)

# this way letter at idx 0 = bottom
for stack in stacks:
    stack.reverse()

# parse moves
for move_line in lines[max_stack_size + 2:]:
    move_parts = move_line.split(' ')
    count = int(move_parts[1])
    start = int(move_parts[3]) - 1
    end = int(move_parts[5]) - 1
    letters = stacks[start][-count:]
    # put in reverse on new stack
    # letters.reverse()
    stacks[end].extend(letters)
    # remove from old
    stacks[start] = stacks[start][:-count]

res = ''.join(x[-1] for x in stacks)
print(res)
