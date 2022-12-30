rocks = [(0, 1, 2, 3),
         (1, 0 + 1j, 2 + 1j, 1 + 2j),
         (0, 1, 2, 2 + 1j, 2 + 2j),
         (0, 0 + 1j, 0 + 2j, 0 + 3j),
         (0, 1, 0 + 1j, 1 + 1j)]
jets = [ord(x) - 61 for x in open('data/day17.txt').read()]
tower, cache, top = set(), dict(), 0

TOWER_WIDTH = 7


def is_empty(pos):
    return pos.real in range(TOWER_WIDTH) and pos.imag > 0 and pos not in tower


def check_move(pos, dir, rock):
    return all(is_empty(pos + dir + r) for r in rock)


i, j = 0, 0

for step in range(int(1e12)):
    pos = complex(2, top + 4)  # set start pos
    if step == 2022:
        print(top)

    key = i, j
    if key in cache:  # check for cycle
        _step, _top = cache[key]
        d, m = divmod(1e12 - step, step - _step)
        if m == 0:
            print(top + (top - _top) * d)
            break
    else:
        cache[key] = step, top

    rock = rocks[i]  # get next rock
    i = (i + 1) % len(rocks)  # and inc index

    while True:
        jet = jets[j]  # get next jet
        j = (j + 1) % len(jets)  # and inc index

        if check_move(pos, jet, rock):
            pos += jet  # maybe move side
        if check_move(pos, -1j, rock):
            pos += -1j  # maybe move down
        else:
            break  # can't move down

    tower |= {pos + r for r in rock}  # add rock to tower
    top = max(top, pos.imag + [1, 0, 2, 2, 3][i])  # compute new top
