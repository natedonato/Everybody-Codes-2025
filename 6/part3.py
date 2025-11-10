with open("./input3.txt") as file:
    input = file.read()

max_dist = 1000
repeat_count = 1000

input = input * repeat_count
l = len(input)

initial = input[:max_dist]
knight_count = initial.count("A")
sword_count = initial.count("B")
archery_count = initial.count("C")

pair_count = 0

for i in range(l):
    left = right = None

    if i + max_dist < l:
        right = input[i + max_dist]

    if i - max_dist - 1 >= 0:
        left = input[i - max_dist - 1]

    c = input[i]

    if right == "A":
        knight_count += 1

    if right == "B":
        sword_count += 1

    if right == "C":
        archery_count += 1

    if left == "A":
        knight_count -= 1

    if left == "B":
        sword_count -= 1

    if left == "C":
        archery_count -= 1

    if c == "a":
        pair_count += knight_count

    if c == "b":
        pair_count += sword_count

    if c == "c":
        pair_count += archery_count

print(pair_count)
