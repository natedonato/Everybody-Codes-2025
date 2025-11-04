with open("everybody_codes_e2025_q01_p3.txt", "r") as file:
    input = file.read().split("\n")

names = input[0].split(",")
dirs = input[2].split(",")

for dir in dirs:
    steps = int(dir[1:])
    if dir[0] == "L":
        steps *= -1

    i = (0 + steps) % len(names)
    names[0], names[i] = names[i], names[0]

print(names[0])
