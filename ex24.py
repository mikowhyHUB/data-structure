'''. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]'''

d1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
      {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
new_d = set()

for i in d1:
    for j in i.values():
        if j not in new_d:
            new_d.add(j)
print(new_d)
