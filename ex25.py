'''Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}'''
import itertools

d1 = {'1': ['a', 'b'], '2': ['c', 'd']}

for i in itertools.product(*[d1[k] for k in sorted(d1.keys())]):
    print(''.join(i))
