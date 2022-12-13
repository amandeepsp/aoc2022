from dataclasses import dataclass
import numpy as np


@dataclass
class Knot:
    x: int
    y: int

    def __sub__(self, knot):
        return Knot(self.x - knot.x, self.y - knot.y)

    def norm(self):
        return np.linalg.norm([self.x, self.y])


len_rope = 10
rope = [Knot(0, 0) for _ in range(len_rope)]
moves = []
t_visited = {(0, 0)}

with open("data/day9.txt", "r") as infile:
    for line in infile:
        (direction, amt) = line.strip().split()
        moves.append((direction, int(amt)))

for direction, amount in moves:
    for _ in range(amount):
        match direction:
            case 'R':
                rope[0].x += 1
            case 'L':
                rope[0].x -= 1
            case 'U':
                rope[0].y += 1
            case 'D':
                rope[0].y -= 1
        for k in range(len_rope - 1):
            if (rope[k] - rope[k + 1]).norm() >= 2:  # Norm of one step removed is at max sqrt(2)
                rope[k + 1].x += np.sign(rope[k].x - rope[k + 1].x)
                rope[k + 1].y += np.sign(rope[k].y - rope[k + 1].y)
                if k + 1 == len(rope) - 1:
                    t_visited.add((rope[len_rope - 1].x, rope[len_rope - 1].y))

# len_rope = 2 for Part 1
print(len(t_visited))
