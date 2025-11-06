import math

with open("./input3.txt","r") as file:
    input = file.read()

input = input.split("\n")

first_gear = int(input[0])
last_gear = int(input[-1])
middle_gears = input[1:-1]

current_rotations = 100
current_teeth = first_gear

for gearset in middle_gears:
    (gear1, gear2) = list(map(lambda x: int(x), gearset.split("|")))

    current_teeth_moved = current_rotations * current_teeth
    rotations = current_teeth_moved / gear1
    
    current_rotations = rotations
    current_teeth = gear2

final_rotations = (current_rotations * current_teeth) / last_gear

print(math.floor(final_rotations))