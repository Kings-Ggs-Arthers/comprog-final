# quiz1 page 27

def avg(n):
    total = 0
    for i in n:
        total = total + float(i)
    return total/len(n)


num = input("enter numbers : ").split()
print(avg(num))


def avg(n):
    total = 0
    for i in range(len(n)):
        total = total + float(n[i])
    return total/len(n)

num = input('Enter numbers : ').split()
print(avg(num))


# quiz 2

# allnum = [e for e in input("Enter your list : ").split()]

# for i in range(len(allnum)):
#     if allnum[i] == "6":
#         n = i + 1

#         summ = 0
#         for i in range(n):
#             summ += i
#         print(summ)
