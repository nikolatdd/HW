def Factorial(n):
    if n <= 0:
        print('Not valid')
    elif n == 1:
        return n
    else:
        return n*Factorial(n-1)

print(Factorial(5))
