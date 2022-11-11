'''Write a Python program to check a list is empty or not.'''

l = []
l2 = [1, 2, 3]


def checking(l):
    if not l:
        print('this list is empty.')
    else:
        print('its all good.')


checking(l)
checking(l2)
