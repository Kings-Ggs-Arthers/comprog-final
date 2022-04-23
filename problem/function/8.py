# problem 2


def C(m, n):
    fac_m = 1
    fac_n = 1
    fac_mn = 1

    # m!
    for M in range(1, m+1):
        fac_m *= M

    # n!
    for N in range(1, n+1):
        fac_n *= N

    # (m-n)!
    for MN in range(1, (m-n)+1):
        fac_mn *= MN

    return main(fac_m, fac_n, fac_mn)


def main(fac_m, fac_n, fac_mn):
    calculate = fac_m / (fac_n*fac_mn)
    print(calculate)


m, n = [int(e) for e in input("Enter your num(num1, num2) : ").split(",")]

C(m, n)
