list_a = ['apple', 'bird', 'cat', 'dog']

print('apple' in list_a)
print('car' in list_a)

print(list_a.index('cat'))
# print(list_a.index('umbrella'))

# del list_a


del list_a[1]
print(list_a)


list_a.remove('apple')
print(list_a)
