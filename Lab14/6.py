tuples = ([5,3,6,8,7],[5,2,3,1,4])
tuples_sorted = sorted(tuples, key = lambda t: (t[0],t[1]))
print(tuples_sorted)