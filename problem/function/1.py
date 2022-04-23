# page 9

def find_fac(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac


print(find_fac(5))
