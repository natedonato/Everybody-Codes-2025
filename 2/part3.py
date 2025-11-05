a = [-79705,-16616]

def add(num1, num2):
    [X1, Y1] = num1
    [X2, Y2] = num2
    return [X1 + X2, Y1 + Y2]

def divide(num1, num2):
    [X1, Y1] = num1
    [X2, Y2] = num2
    out = [X1 // X2, Y1 // Y2]
    if X1 < 0:
        out[0] += 1
    if Y1 < 0:
        out[1] += 1
    return out

def multiply(num1, num2):
    [X1, Y1] = num1
    [X2, Y2] = num2
    return [(X1 * X2) - (Y1 * Y2), (X1 * Y2) + (Y1 * X2)]


def shouldEngrave(point):
    result = [0,0]
    
    for _ in range(100):
        result = multiply(result, result)
        result = divide(result, [100_000,100_000])
        result = add(result, point)

        if result[0] > 1000000 or result[1] > 1000000 or result[0] < -1000000 or result[1] < -1000000:
            return False

    return True        

opposite_corner = add(a, [1000,1000])


points = []
for dy in range(1001):
    row = []
    for dx in range(1001):
        row.append(add(a, [dx*1, dy*1]))
    points.append(row)


count = 0
output = ""
for row in points:
    for el in row:
        engrave = shouldEngrave(el)
        if engrave:
            output += "X"
            count += 1
        else:
            output += " "

    output += "\n"

with open("fractal.txt", 'w') as file:
    file.write(output)

print(count)
