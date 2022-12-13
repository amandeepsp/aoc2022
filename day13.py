import functools


def sgn(x: int) -> int:
    if x == 0:
        return 0
    return x // abs(x)


def compare_lists(left: list, right: list) -> int:
    index = 0
    while index < len(left) and index < len(right):
        if isinstance(left[index], int) and isinstance(right[index], int):
            if left[index] == right[index]:
                index += 1
                continue
            else:
                return sgn(left[index] - right[index])
        elif isinstance(left[index], list) or isinstance(right[index], list):
            left_list = [left[index]] if isinstance(left[index], int) else left[index]
            right_list = [right[index]] if isinstance(right[index], int) else right[index]
            list_comparison = compare_lists(left_list, right_list)
            if list_comparison == 0:
                index += 1
                continue
            else:
                return list_comparison

    if len(right) - 1 < index < len(left):
        return 1

    if len(left) - 1 < index < len(right):
        return -1

    return 0


with open("data/day13.txt", "r") as infile:
    part1 = 0
    pairs = infile.read().split("\n\n")
    for i, pair in enumerate(pairs):
        (a, b) = pair.split("\n")
        left, right = eval(a), eval(b)
        if compare_lists(left, right) < 0:
            part1 += (i + 1)

    print(part1)

    infile.seek(0)
    packets = [eval(line.strip()) for line in infile.readlines() if line.strip()]
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare_lists))

    # Part 2
    print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
