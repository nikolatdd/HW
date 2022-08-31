def search_list(pool):
    pos = 5
    for i in range(len(pool)):
        if pool[i] == pos:
            print(f'Pos {i} matches')
        else:
            print('No match')
pool = [1, 2, 5, 9, 10]
search_list(pool)
