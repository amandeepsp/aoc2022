reg = 1
clock = [0] * 241
crt = ['.'] * 240

with open("data/day10.txt", "r") as infile:
    clock_counter = 0
    for command in infile:
        if command.startswith("noop"):
            clock_counter += 1
            clock[clock_counter] = reg
        elif command.startswith("addx"):
            (_, num) = command.strip().split()
            clock[clock_counter] = reg
            clock[clock_counter + 1] = reg
            reg += int(num)
            clock_counter += 2
            clock[clock_counter] = reg

total_strength = 0

for i in range(20, 221, 40):
    total_strength += i * clock[i - 1]

# Part 1
print(total_strength)

# Part 2
for i in range(240):
    if i % 40 in [clock[i] - 1, clock[i], clock[i] + 1]:
        crt[i] = "#"

for row in range(6):
    start = row * 40
    end = start + 40
    print(''.join(crt[start:end]))
