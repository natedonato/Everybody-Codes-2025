a = [-79705, -16616]

def add(num1, num2):
    [X1, Y1] = num1
    [X2, Y2] = num2
    return [X1 + X2, Y1 + Y2]

def divide(num1, num2):
    [X1, Y1] = num1
    [X2, Y2] = num2
    return [int(X1 / X2), int(Y1 / Y2)]

def multiply(num1, num2):
    [X1, Y1] = num1
    [X2, Y2] = num2
    return [(X1 * X2) - (Y1 * Y2), (X1 * Y2) + (Y1 * X2)]

def shouldEngrave(point):
    result = [0, 0]

    for _ in range(100):
        result = multiply(result, result)
        result = divide(result, [100_000, 100_000])
        result = add(result, point)

        if (
            result[0] > 1000000
            or result[1] > 1000000
            or result[0] < -1000000
            or result[1] < -1000000
        ):
            return False

    return True

opposite_corner = add(a, [1000, 1000])

points = []
for dy in range(101):
    row = []
    for dx in range(101):
        row.append(add(a, [dx * 10, dy * 10]))
    points.append(row)

count = 0

for row in points:
    for el in row:
        # print(el)
        engrave = shouldEngrave(el)
        if engrave:
            print("x", end="")
            count += 1
        else:
            print("·", end="")
    print("")

print(count)
