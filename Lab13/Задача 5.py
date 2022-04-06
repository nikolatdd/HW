import re 
count = 1
for i in dir(re): 
    if 'find' in i:
        count+=1
print(count)