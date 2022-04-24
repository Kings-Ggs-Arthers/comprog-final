data = [x for x in range(1, 6)]
print(data)

data1 = []
for e in range(1, 6):
    data1.append(e)
print(data1)


numbers = [1, 2, 3, 4, 5, 6, 7]

power_of_two = [2 ** x for x in numbers]
print(power_of_two)

power_of_two_range = [2 ** x for x in range(30) if x % 5 ==0]
print(power_of_two_range)



words = ['automoblie', 'car', 'anger', 'fox', 'anchor']

words1 = [word.upper() if word.startswith('a') else word for word in words]
words2 = [word.upper() for word in words if word.startswith('a')]


print(words)
print(words1)
print(words2)
