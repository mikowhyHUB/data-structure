'''
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']'''

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


def removing(l):
    l.pop(0)
    l.pop(3)
    l.pop(3)
    return l


print(removing(sample))
