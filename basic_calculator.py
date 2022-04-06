res = 0
def add(x, y):
    global res
    res = x + y

def substract(x, y):
    global res
    res = x - y

def multiplication(x, y):
    global res
    res = x * y

def division(x, y):
    global res
    res = x / y

def print_res():
    global res
    print(res)


