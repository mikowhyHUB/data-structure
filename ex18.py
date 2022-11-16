'''Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). '''


def making_dict(sample):
    d = {}
    for i in range(1, sample+1):
        d.update({i: i*i})
    print(d)


making_dict(5)
