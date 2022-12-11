from collections import defaultdict
from math import prod

monkeys = [
    {
        'start': [56, 52, 58, 96, 70, 75, 72],
        'op': lambda x: x * 17,
        'test': 11,
        'true': 2,
        'false': 3
    }, {
        'start': [75, 58, 86, 80, 55, 81],
        'op': lambda x: x + 7,
        'test': 3,
        'true': 6,
        'false': 5
    }, {
        'start': [73, 68, 73, 90],
        'op': lambda x: x * x,
        'test': 5,
        'true': 1, 'false': 7
    }, {
        'start': [72, 89, 55, 51, 59],
        'op': lambda x: x + 1,
        'test': 7,
        'true': 2, 'false': 7
    }, {
        'start': [76, 76, 91],
        'op': lambda x: x * 3,
        'test': 19,
        'true': 0, 'false': 3
    }, {
        'start': [88],
        'op': lambda x: x + 4,
        'test': 2,
        'true': 6, 'false': 4
    }, {
        'start': [64, 63, 56, 50, 77, 55, 55, 86],
        'op': lambda x: x + 8,
        'test': 13,
        'true': 4, 'false': 0
    }, {
        'start': [79, 58],
        'op': lambda x: x + 6,
        'test': 17,
        'true': 1, 'false': 5
    }
]

monkey_items = [monkey['start'] for monkey in monkeys]

num_inspections = defaultdict(int)

lcm = prod([monkey['test'] for monkey in monkeys])  # All numbers are prime

for _ in range(10_000):
    for monkey_num, monkey in enumerate(monkeys):
        for item in monkey_items[monkey_num]:
            num_inspections[monkey_num] += 1
            worry_level = monkey['op'](item) % lcm
            test = worry_level % monkey['test'] == 0
            monkey_items[monkey['true'] if test else monkey['false']].append(worry_level)
        monkey_items[monkey_num] = []

inspection_vals = sorted(num_inspections.values())

print(inspection_vals[-1] * inspection_vals[-2])
