calories = []

with open("data/day1.txt", "r") as infile:
    curr_group = []
    for line in infile:
        if not line.strip():
            calories.append(curr_group)
            curr_group = []
        else:
            calorie_num = int(line.strip())
            curr_group.append(calorie_num)

calorie_sums = [sum(cals) for cals in calories]
calorie_sums = sorted(calorie_sums)

# Part 1
print(calorie_sums[-1])
# Part 2
print(sum(calorie_sums[-3:]))
