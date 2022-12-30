cubes = []
neighbours = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

with open("data/day18.txt", "r") as infile:
    for line in infile:
        cube_start = tuple(map(int, line.strip().split(',')))
        cubes.append(cube_start)

exposed = 0
for cube in cubes:
    for neighbour in neighbours:
        exact_neighbour = tuple(ai + bi for ai, bi in zip(cube, neighbour))
        if exact_neighbour not in cubes:
            exposed += 1

print(exposed)

minout = [min(c[i] - 1 for c in cubes) for i in range(3)]
maxout = [max(c[i] + 1 for c in cubes) for i in range(3)]


def in_space(cube):
    return all(minout[i] <= cube[i] <= maxout[i] for i in range(3))


exposed_outside = 0
seen = set()
queue = [tuple(maxout)]
while queue:
    curr_cube = queue.pop(0)
    if curr_cube in cubes:
        exposed_outside += 1
        continue
    if curr_cube not in seen:
        seen.add(curr_cube)
        for neighbour in neighbours:
            exact_neighbour = tuple(ai + bi for ai, bi in zip(curr_cube, neighbour))
            if in_space(exact_neighbour):
                queue.append(exact_neighbour)

print(exposed_outside)
