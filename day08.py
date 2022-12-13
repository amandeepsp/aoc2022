def get_visible(arr):
    def get_visible_ltr(arr):
        max_till_now = -1
        visible_indices = []
        for index, height in enumerate(arr):
            if max_till_now == -1:
                max_till_now = height
                visible_indices.append(index)
            elif max_till_now < height:
                visible_indices.append(index)
                max_till_now = height
        return visible_indices

    ltr_visible_indices = get_visible_ltr(arr)
    rtl_visible_indices = [len(arr) - idx - 1 for idx in get_visible_ltr(reversed(arr))]
    return set(ltr_visible_indices + rtl_visible_indices)


def tree_view(ipos, jpos):
    tree_limit_top = 0
    tree_limit_bottom = 0
    tree_limit_right = 0
    tree_limit_left = 0

    # Checking Top
    for i in range(ipos - 1, -1, -1):
        if grid[i][jpos] < grid[ipos][jpos]:
            tree_limit_top += 1
        elif grid[i][jpos] >= grid[ipos][jpos]:
            tree_limit_top += 1
            break
    # Checking Left
    for j in range(jpos - 1, -1, -1):
        if grid[ipos][j] < grid[ipos][jpos]:
            tree_limit_left += 1
        elif grid[ipos][j] >= grid[ipos][jpos]:
            tree_limit_left += 1
            break
    # Checking Right
    for i in range(jpos + 1, len(grid[ipos])):
        if grid[ipos][i] < grid[ipos][jpos]:
            tree_limit_right += 1
        elif grid[ipos][i] >= grid[ipos][jpos]:
            tree_limit_right += 1
            break
    # Checking Bottom
    for j in range(ipos + 1, len(grid)):
        if grid[j][jpos] < grid[ipos][jpos]:
            tree_limit_bottom += 1
        elif grid[j][jpos] >= grid[ipos][jpos]:
            tree_limit_bottom += 1
            break

    return tree_limit_top * tree_limit_left * tree_limit_bottom * tree_limit_right


with open("data/day8.txt", "r") as infile:
    grid = [[int(item) for item in line.strip()] for line in infile.readlines()]
    transpose_grid = list(zip(*grid))
    row_visibles = []
    col_visibles = []
    for index, row in enumerate(grid):
        row_visibles += [(index, visible_index) for visible_index in get_visible(row)]
    for index, col in enumerate(transpose_grid):
        col_visibles += [(visible_index, index) for visible_index in get_visible(col)]

    visibles = set(row_visibles + col_visibles)
    # Part 1
    print(len(visibles))

    # Part 2
    side = len(grid)
    max_score = 0

    for i in range(side):
        for j in range(side):
            max_score = max(max_score, tree_view(i, j))
    print(max_score)
