with open("everybody_codes_e2025_q01_p2.txt", "r") as file:
    input = file.read().split("\n")

names = input[0].split(",")
directions = input[2].split(",")

i = 0

for dir in directions:
    steps = int(dir[1:])
    if dir[0] == "L":
        steps *= -1

    i += steps
    i %= len(names)

print(names[i])
