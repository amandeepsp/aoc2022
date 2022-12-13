scores = {'X': 1, 'Y': 2, 'Z': 3}

p2_loses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
p2_wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
p2_draws = {'A': 'X', 'B': 'Y', 'C': 'Z'}


def find_score_simple(p1, p2) -> int:
    score = scores[p2]
    if p2_loses[p1] == p2:
        return score
    elif p2_wins[p1] == p2:
        return score + 6
    else:
        return score + 3


def find_score_strategy(p1, p2) -> int:
    match p2:
        case 'X':
            return scores[p2_loses[p1]]
        case 'Y':
            return scores[p2_draws[p1]] + 3
        case 'Z':
            return scores[p2_wins[p1]] + 6

    raise "Invalid case"


total_score_part_1 = 0
total_score_part_2 = 0

with open("data/day2.txt", "r") as infile:
    for line in infile:
        (p1, p2) = line.strip().split()
        total_score_part_1 += find_score_simple(p1, p2)
        total_score_part_2 += find_score_strategy(p1, p2)

print(total_score_part_1, total_score_part_2)
