with open("./input1.txt", "r") as file:
    input = file.read()

input = list(map(int, input.split(",")))

wheel_size = 32

def opposite(n):
    opp = wheel_size//2 + n
    opp %= wheel_size
    if opp == 0:
        opp = wheel_size
    return opp

prev = None
count = 0
for n in input:
    if opposite(n) == prev:
        count += 1
    prev = n 

print(count)
