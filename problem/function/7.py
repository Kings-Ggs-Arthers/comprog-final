# problem 1

def real_Number(*num):
    return min(num)


num1, num2, num3 = [int(e) for e in input(
    "Enter your num(num1, num2, num3) : ").split(",")]

print(real_Number(num1, num2, num3))
