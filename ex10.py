'''Write a Python program to add an item in a tuple.'''

t = (1, 2, 3)
t = t + (9,)

print(t)

t = t[:2] + (8,) + t[:2]
print(t)
