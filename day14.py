rocks = set()
sands = set()

with open("data/day14.txt") as infile:
    for line in infile:
        pairs_str = line.strip().split(' -> ')
        pairs = [tuple(map(int, pair.split(','))) for pair in pairs_str]
        for pair0, pair1 in zip(pairs[:-1], pairs[1:]):
            dx = range(min(pair0[0], pair1[0]), max(pair0[0], pair1[0]) + 1)
            dy = range(min(pair0[1], pair1[1]), max(pair0[1], pair1[1]) + 1)
            rocks.update({(x, y) for x in dx for y in dy})

max_y = max([y for _, y in rocks])

start = (500, 0)
pos = start
count = 0

part1 = part2 = None

while True:
    if pos in rocks:
        pos = start

    if pos[1] > max_y and not part1:
        part1 = count

    if (pos[0], pos[1] + 1) not in rocks and pos[1] <= max_y:
        pos = (pos[0], pos[1] + 1)
    elif (pos[0] - 1, pos[1] + 1) not in rocks and pos[1] <= max_y:
        pos = (pos[0] - 1, pos[1] + 1)
    elif (pos[0] + 1, pos[1] + 1) not in rocks and pos[1] <= max_y:
        pos = (pos[0] + 1, pos[1] + 1)
    else:
        count += 1
        rocks.add(pos)

    if pos == start:
        # Fully Filled
        part2 = count
        break

print(part1)
print(part2)

