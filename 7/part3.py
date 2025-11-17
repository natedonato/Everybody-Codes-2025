with open("./input3.txt") as file:
    input = file.read()

input = input.split("\n")
names = input[0].split(",")
rules = list(map(lambda x: x.split(" > "), input[2:]))

graph = {}

for rule in rules:
    parent = rule[0]
    children = rule[1].split(",")
    graph[parent] = {*children}

def checkName(name):
    prev = None
    for c in name:
        if prev and c not in graph[prev]:
            return False
        prev = c
    return True

valid_prefixes = []

for i in range(len(names)):
    name = names[i]
    if checkName(name):
        valid_prefixes.append(name)

unique_names = set()

def make_possible_names(prev_name):
    prev_char = prev_name[-1]
    length = len(prev_name)

    if length > 11:
        return

    if length >= 7:
        unique_names.add(prev_name)

    if prev_char in graph:
        next_chars = graph[prev_char]

        for next_char in next_chars:
            make_possible_names(prev_name + next_char)

for name in valid_prefixes:
    make_possible_names(name)

print(len(unique_names))
