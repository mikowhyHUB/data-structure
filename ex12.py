'''Write a Python program to find the repeated items of a tuple'''

t = (1, 2, 3, 4, 5, 4, 2)

# new = [i for i in t if i in t]
new = []
for i in t:
    if i in t:
        new.append(i)


print(new)
