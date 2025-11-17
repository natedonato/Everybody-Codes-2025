with open("./input2.txt") as file:
    input = file.read()

input = input.split("\n")

trieroot = {'end': False}

for line in input:
    [id, s] = line.split(":")
    
    current = trieroot
    for c in s:
        if c not in current:
            current[c] = {'end': False}
        current = current[c]
    current['end'] = True
    current['id'] = id

for p1 in len(input):
    for p2 in len(input):
        current = [trieroot]
        valid = True
        for i in range(max_score):
            c1 = p1[i]
            c2 = p2[i]
            for node in current:
