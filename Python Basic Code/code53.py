#Q53. Sort dictionary by values d = {'b':2,'a':1}?

d = {'b': 2, 'a': 1}

sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))

print(sorted_d)
