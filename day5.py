import re
from collections import namedtuple

stacks = ['ZJNWPS', 'GST', 'VQRLH', 'VSTD', 'QZTDBMJ', 'MWTJDCZL', 'LPMWGTJ', 'NGMTBFQH', 'RDGCPBQW']
stacks_part_2 = stacks.copy()

line_pattern = re.compile(r"move (?P<amount>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)")

Movement = namedtuple('Movement', 'amount from_stack to_stack')


def execute_movement(stacks: list[str], movement: Movement, reverse_move: bool = True):
    move_items = stacks[movement.from_stack - 1][-movement.amount:]
    stacks[movement.to_stack - 1] += ''.join(reversed(move_items) if reverse_move else move_items)
    stacks[movement.from_stack - 1] = stacks[movement.from_stack - 1].removesuffix(''.join(move_items))


with open("data/day5.txt", "r") as infile:
    for line in infile:
        line_match = line_pattern.match(line)
        movement = Movement(
            amount=int(line_match.group('amount')),
            from_stack=int(line_match.group('from_stack')),
            to_stack=int(line_match.group('to_stack'))
        )
        execute_movement(stacks, movement)
        execute_movement(stacks_part_2, movement, reverse_move=False)

print("".join([stack[-1] for stack in stacks]))
print("".join([stack[-1] for stack in stacks_part_2]))
