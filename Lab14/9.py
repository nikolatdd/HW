lst = [1,2,3]

count_odd = len(list(filter(lambda x: (x%2==1), lst)))
count_even = len(list(filter(lambda y: (y%2==0), lst))) 
print(f'count_odd {count_odd}')
print(f'count_even {count_even}')