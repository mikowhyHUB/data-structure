'''Write a Python program to clone or copy a list.'''


original = [1, 2, 'three', 3.14]


def copying(l):
    new_one = []
    new_one = [i for i in l]
    return new_one


print(copying(original))
