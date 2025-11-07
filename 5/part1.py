with open("input1.txt", "r") as file:
    input = file.read()

sword_id = input.split(":")[0]
input = input.split(":")[1]
input = input.split(",")
input = list(map(lambda el: int(el), input))


next_segment = [None] * 3
segments = [next_segment]

for num in input:
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

print(out)
