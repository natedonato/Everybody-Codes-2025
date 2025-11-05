input = "A=[155,59]"
input = input[3:-1]
print(input)

a = list(map(lambda x: int(x), input.split(",")))

def add(num1, num2):
    return [num1[0] + num2[0], num1[1] + num2[1]]

def divide(num1, num2):
    return [num1[0] // num2[0], num1[1] // num2[1]]


def multiply(num1, num2):
    return [num1[0] * num2[0] - num1[1] * num2[1], num1[0] * num2[1] + num1[1] * num2[0]]


result = [0,0]

for _ in range(3):
    result = multiply(result, result)
    result = divide(result, [10,10])
    result = add(result, a)

print(result)
