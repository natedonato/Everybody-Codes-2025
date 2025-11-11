with open("./input1.txt") as file:
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

for name in names:
    if checkName(name):
        print(name)
