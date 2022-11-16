'''Write a Python program to map two lists into a dictionary.'''

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

d = dict(zip(l1, l2))
print(d)
