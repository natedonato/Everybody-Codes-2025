import math

with open("./input1.txt","r") as file:
    input = file.read()

input = list(map(lambda x: int(x), input.split("\n")))

rotations = 2025

for i in range(len(input)):
    gear = input[i]
    teeth_moved = rotations * gear
    if i < len(input) - 1:
        next_gear = input[i+1]
        next_rotations = teeth_moved / next_gear
        rotations = next_rotations

print(math.floor(rotations))