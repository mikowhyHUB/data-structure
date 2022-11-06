#Write a Python algorithm which returns the maximum of the list without using any predefined function in Python.
def maximum(l):
    max_list = l[0]
    for i in l:
        if max_list < i:
            max_list = i
    print(max_list)

lst = [2,1,64,3,67,78,23]
maximum(lst)