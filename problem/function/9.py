# problem 3


def prime_Number(num):
    x = 2

    while x <= num-1:
        if num % x == 0:
            break
        x += 1

    if x == num:
        return True
    else:
        return False


while True:
    num = int(input("Enter your num : "))
    if num < 2:
        break
    print(prime_Number(num))
