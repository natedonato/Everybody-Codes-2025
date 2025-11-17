with open("./input1.txt") as file:
    input = file.read()

input = list(map(lambda e: e[2:], input.split("\n")))

print(input)


for idx in range(len(input)):
    possible_child = input[idx]
    parent_idxes = [0,1,2]
    parent_idxes.remove(idx)

    s1 = 0
    s2 = 0
    valid = True
    for i in range(len(possible_child)):
        c = possible_child[i]
        c1 = input[parent_idxes[0]][i]
        c2 = input[parent_idxes[1]][i]

        if c != c1 and c != c2:
            valid = False
            break

        if c1 == c:
            s1 += 1
        if c2 == c:
            s2 += 1

    if not valid:
        continue
    
    print(s1,s2)
    print(s1 * s2)