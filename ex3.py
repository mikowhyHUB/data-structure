#Write a Python algorithm that returns the list of duplicate elements of a given list. Example if L = [7, 23, 5, 12, 7, 19, 23, 12, 29], the algorithm returns the list: [7, 23, 12]

l = [7, 23, 5, 12, 7, 19, 23, 12, 29]

def duplicate(l):
    dup_list = []
    for i in l:
        if l.count(i)>1 and i not in dup_list:
            dup_list.append(i)
    print(dup_list)

duplicate(l)