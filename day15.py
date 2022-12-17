import re

line_pattern = re.compile(
    r"Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)")
closest_beacons = {}


def manhatten_dist(coords1, coords2):
    (x1, y1) = coords1
    (x2, y2) = coords2
    return abs(x2 - x1) + abs(y2 - y1)


with open("data/day15.txt") as infile:
    for line in infile:
        line_match = line_pattern.match(line)
        sensor_pos = (int(line_match.group('sx')), int(line_match.group('sy')))
        closest_beacon_pos = (int(line_match.group('bx')), int(line_match.group('by')))
        closest_beacons[sensor_pos] = closest_beacon_pos


def non_beacon_positions_at(y):
    ranges = []
    for sensor_pos, closest_beacon_pos in closest_beacons.items():
        d = manhatten_dist(sensor_pos, closest_beacon_pos)
        if sensor_pos[1] + d >= y >= sensor_pos[1] - d:
            ysy_dist = abs(y - sensor_pos[1])
            range_start = sensor_pos[0] - d + ysy_dist
            range_end = sensor_pos[0] + d - ysy_dist
            ranges.append((range_start, range_end))

    reduced_ranges = []
    for begin, end in sorted(ranges):
        if reduced_ranges and reduced_ranges[-1][1] >= begin - 1:
            reduced_ranges[-1] = (reduced_ranges[-1][0], max(reduced_ranges[-1][1], end))
        else:
            reduced_ranges.append((begin, end))

    return reduced_ranges


# Part 1
reduced_ranges = non_beacon_positions_at(2000000)
count = 0
for begin, end in reduced_ranges:
    count += (end - begin)
print(count)

# Part 2
for y in range(4000000):
    curr_ranges = non_beacon_positions_at(y)
    if len(curr_ranges) > 1 and curr_ranges[0][1] + 2 == curr_ranges[1][0]:
        print((curr_ranges[0][1] + 1) * 4000000 + y)
        break
