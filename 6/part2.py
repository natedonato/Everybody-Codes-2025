with open("./input2.txt") as file:
    input = file.read()

knight_count = 0
sword_count = 0
archery_count = 0

pair_count = 0

for c in input:
    if c == "A":
        knight_count += 1

    if c == "a":
        pair_count += knight_count

    if c == "B":
        sword_count += 1

    if c == "b":
        pair_count += sword_count

    if c == "C":
        archery_count += 1

    if c == "c":
        pair_count += archery_count

print(pair_count)
