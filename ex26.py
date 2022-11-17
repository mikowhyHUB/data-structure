'''Write a Python program to find the highest 3 values of corresponding keys in a dictionary.'''

d2 = {'a': 300, 'b': 200, 'd': 400, 'g': 7, 'xd': 420, 'jp': 2137}

outcome = sorted(d2.values(), reverse=True)
print(*outcome[0:3])
