file = open('in.txt', 'r')

line = file.readline()

signal_length = 4

for start_idx in range(len(line) - signal_length + 1):
    if len(set(line[start_idx:start_idx + signal_length])) == signal_length:
        print(start_idx + signal_length)
        break
