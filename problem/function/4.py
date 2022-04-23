# quiz 1

def sum_digits(num):
    result = [int(e) for e in num]
    return sum(result)


num = input('Enter your num : ')
print('Your result is', sum_digits(num))

