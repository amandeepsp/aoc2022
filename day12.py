import queue

grid = []

with open("data/day12.txt", "r") as infile:
    for line in infile:
        grid.append(list(line.strip()))

grid_len = len(grid)
grid_0_len = len(grid[0])


def elevation_of(coords: (int, int)):
    (i, j) = coords
    match grid[i][j]:
        case 'S':
            return 0
        case 'E':
            return 25
        case el:
            return ord(el) - ord('a')


def get_node(target):
    for i in range(grid_len):
        for j in range(grid_0_len):
            if grid[i][j] == target:
                return i, j


start_node = get_node('S')
end_node = get_node('E')
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()
queue = queue.Queue()
queue.put((end_node, 0))
min_level = None
while not queue.empty():
    (node, level) = queue.get()
    if node in visited:
        continue
    visited.add(node)
    if grid[node[0]][node[1]] == 'S':
        # Part 1
        print(level)
        break
    if grid[node[0]][node[1]] == 'a' and not min_level:
        min_level = level
    for direction in directions:
        child_node = tuple([a + b for a, b in zip(node, direction)])
        if 0 <= child_node[0] < grid_len and 0 <= child_node[1] < grid_0_len:
            if child_node not in visited:
                if -elevation_of(child_node) + elevation_of(node) <= 1:
                    queue.put((child_node, level + 1))

# Part 2
print(min_level)
