# for loop

data = ['apple', 'bird', 'cat']

# for e in data:
#     print(e)

# for e in range(len(data)):
#     print(e)


# score = [0, 0, 0, 0]
# for e in range(len(score)):
#     score[e] = int(input("Enter a score : "))
# print(score)

score = [int(e) for e in input("enter a score : ").split()]
print(score)
