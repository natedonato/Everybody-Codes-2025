with open("input3.txt", "r") as file:
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

    properties = []

    quality = ""
    for s in segments:
        quality += str(s[1])
    quality = int(quality)
    properties.append(quality)

    for seg in segments:
        seg = list(filter(lambda e: e is not None, seg))
        seg = list(map(lambda e: str(e), seg))
        properties.append(int("".join(seg)))

    properties.append(int(sword_id))

    return properties


input = input.split("\n")

all_properties = []

for line in input:
    all_properties.append(getQuality(line))

all_properties.sort(reverse=True)

checksum = 0

for i in range(len(all_properties)):
    sid = all_properties[i][-1]
    checksum += sid * (i + 1)

print(checksum)
