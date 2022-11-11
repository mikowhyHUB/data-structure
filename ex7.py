'''Write a Python function that takes two lists and returns True if they have at least one common member.'''

l1 = [1, 't2', 3, 4, 2]
l2 = ['one', 2, 5, 6, 7]

for i in l1:
    for j in l2:
        if i == j:
            print('Common member')
