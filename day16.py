import re
import itertools
from functools import cache
from collections import defaultdict

line_pattern = re.compile(
    r"^Valve (\w+) has flow rate=(\d+); tunnel(s?) lead(s?) to valve(s?)([\s\w,]+)$")

vertices = set()
flows = dict()
distances = defaultdict(lambda: 1e8)

with open("data/day16.txt", "r") as infile:
    for line in infile:
        line_match = line_pattern.match(line)
        vertex = line_match.group(1)
        flow_rate = int(line_match.group(2))
        adjs = line_match.group(6).strip().split(", ")

        vertices.add(vertex)
        if flow_rate > 0:
            flows[vertex] = flow_rate
        for adj in adjs:
            distances[vertex, adj] = 1

for k, i, j in itertools.product(vertices, vertices, vertices):
    distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])


@cache
def search(time, u='AA', valid_vs=frozenset(flows), elephant=False):
    max_flow = 0
    for v in valid_vs:
        if distances[u, v] < time:
            expected_flows = flows[v] * (time - distances[u, v] - 1) + \
                             search(time - distances[u, v] - 1, v, valid_vs - {v}, elephant)
            max_flow = max(max_flow, expected_flows)

    if elephant:
        max_flow = max(max_flow, search(26, valid_vs=valid_vs))

    return max_flow


print(search(30))
print(search(26, elephant=True))
