# quiz1 page 57


import random

# ran = []

# for i in range(10):
#     x = random.random()
#     ran.append(x)

# ran1 = [random.random() for i in range(10)]

# print(ran)
# print(ran1)


# quiz 2

# ran = [random.random() for i in range(10)]
# ran = [e for e in ran if e > 0.5]
# print(ran)


# quiz 3

account_no = [47362837, 39485743, 18273648, 38473819]

account_no = [int(str(acc_no)[:4]) for acc_no in account_no]

print(account_no)
