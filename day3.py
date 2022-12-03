with open("data/day3.txt", "r") as infile:
    rucksacks = [line.strip() for line in infile]


    def score_common_items(common_items: set) -> int:
        score = 0
        for common_item in common_items:
            if ord(common_item) >= ord('a'):
                score += ord(common_item) - ord('a') + 1
            elif ord('A') <= ord(common_item) < ord('a'):
                score += ord(common_item) - ord('A') + 27
            else:
                raise f"Invalid char {common_item}"
        return score


    common_items_score1 = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        group1 = rucksack[:mid]
        group2 = rucksack[mid:]
        common_items = set.intersection(set(group1), set(group2))
        common_items_score1 += score_common_items(common_items)

    # Part 1
    print(common_items_score1)

    common_items_score2 = 0
    groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
    for group in groups:
        group_sets = [set(items) for items in group]
        common_items = set.intersection(*group_sets)
        common_items_score2 += score_common_items(common_items)

    # Part 2
    print(common_items_score2)
