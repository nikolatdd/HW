def search_list(pool):
    num = 5
    for i in range(len(pool)):
        if pool[i] == num:       
            return i       
def print_result(result):
	print(result)

pool = [1, 2, 5, 9, 10]
result = search_list(pool)
print_result(result)