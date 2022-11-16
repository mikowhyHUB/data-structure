'''Write a Python program to sort a given dictionary by key.'''

d = {13: 169, 14: 196, 15: 225, 3: 9, 4: 16, 5: 25, 6: 36,
     7: 49, 8: 64,  10: 100, 11: 121, 12: 144, 1: 1, 2: 4, 9: 81}

for i in sorted(d):
    print("%s:%s" % (i, d[i]))
