#Write an algorithm in python as a function which takes as parameter a list of numbers L and which returns the minimum of the list without using any predefined function in Python.

def minimum(l):
    min_list =l[0]
    for i in l:
        if min_list > i:
            min_list = i
    print(min_list)


l = [1,2,3,12,50]
minimum(l)