from collections import Counter

message = open("data/day6.txt", "r").read()


def find_start_of_packet(message: str, len: int) -> int:
    for idx, char in enumerate(message):
        if list(Counter(message[idx - len:idx]).values()) == [1] * len:
            return idx
    return -1


print(find_start_of_packet(message, 4))
print(find_start_of_packet(message, 14))
