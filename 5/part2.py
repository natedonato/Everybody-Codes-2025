with open("input2.txt", "r") as file:
    input = file.read()


def getQuality(line):
    sword_id = line.split(":")[0]

    line = line.split(":")[1]
    line = line.split(",")
    line = list(map(lambda el: int(el), line))

    next_segment = [None] * 3

    segments = [next_segment]

    for num in line:
        if segments[-1][1] is None:
            segments[-1][1] = num
        else:
            placed = False
            for s in segments:
                prev = s[1]
                if num < prev:
                    if s[0] is None:
                        s[0] = num
                        placed = True
                        break
                elif num > prev:
                    if s[2] is None:
                        s[2] = num
                        placed = True
                        break

            if not placed:
                segments.append([None, num, None])
                continue

    out = ""
    for s in segments:
        out += str(s[1])
    return int(out)


input = input.split("\n")

qualities = []

for line in input:
    qualities.append(getQuality(line))

#print(qualities)
print(max(qualities) - min(qualities))
