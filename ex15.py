'''Write a Python program to convert a tuple to a dictionary.'''

t = ((1, "w"), (2, "z"))
print(dict((y, x) for x, y in t))
