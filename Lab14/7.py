dicts = ({'Letter':'A','Number':3},{'Letter':'B','Number':4})
dicts_sorted = sorted(dicts, key = lambda d: (d['Letter'],d['Number']))
print(dicts_sorted)