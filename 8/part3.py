with open("./input3.txt", "r") as file:
    input = file.read()

wheel_size = 256

input = list(map(int, input.split(",")))
for i in range(len(input)):
    if input[i] == wheel_size:
        input[i] = 0

prev = input[0]

# RELATIVE to root
nails = [ [0] * wheel_size for _ in range(wheel_size)]

def offset(prev, curr):
    diff = curr - prev
    if diff < 0:
        diff += wheel_size
    return diff % wheel_size

total_knots = 0

for index in range(1, len(input)):    
    nail = input[index]
   
    nails[prev][offset(prev, nail)] += 1
    nails[nail][offset(nail, prev)] += 1
    prev = nail



def getStringsCut(segment):
    count = 0
    for i in range(segment[0] + 1, segment[1]):
        middle_nail = i
        j = (segment[1] + 1)  % wheel_size
        while j != segment[0]:
            count += nails[middle_nail][offset(middle_nail, j)]
            j += 1
            j %= wheel_size

    count += nails[segment[0]][offset(segment[0], segment[1])]
    
    return count

most_cut = 0
for i in range(wheel_size):
    for j in range(i+1, wheel_size):
        segment = [i,j]
        cuts = getStringsCut(segment)
        most_cut = max(most_cut, cuts)

    print(i / wheel_size)

print(most_cut)