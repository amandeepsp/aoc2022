def range_fully_contains(r1: list, r2: list) -> bool:
    start_r1 = r1[0]
    start_r2 = r2[0]
    end_r1 = r1[1]
    end_r2 = r2[1]
    return start_r1 <= start_r2 and end_r2 <= end_r1


def range_overlap(r1: list, r2: list) -> bool:
    start_r1 = r1[0]
    start_r2 = r2[0]
    end_r1 = r1[1]
    end_r2 = r2[1]
    return start_r1 <= end_r2 and start_r2 <= end_r1


with open("data/day4.txt", "r") as infile:
    fully_contains_count = 0
    any_overlap_count = 0

    for line in infile:
        ranges = [[int(x) for x in range.split('-')] for range in line.strip().split(',')]
        fully_contains_count += range_fully_contains(*ranges) or range_fully_contains(*reversed(ranges))
        any_overlap_count += range_overlap(*ranges)

    print(fully_contains_count)
    print(any_overlap_count)
