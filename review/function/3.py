def multiply1(num1, num2):
    return num1*num2

print(multiply1(2, 3))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4))
