with open("./input1.txt") as file:
    input = file.read()

knight_count = 0
pair_count = 0

for c in input:
    if c == "A":
        knight_count += 1

    if c == "a":
        pair_count += knight_count

print(pair_count)
