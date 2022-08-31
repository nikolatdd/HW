def Add():
    prod = str(input('\nWhat would you like to add?\n'))
    cart.append(prod)
def Remove():
    s = str(input(f'\nWhat would you like to remove {cart}?'))
    if s in cart:
        cart.remove(s)
def clear():
    global cart
    print('\nEmptying your cart...')
    cart = []
def show():
    print(f'\nYour current cart:\n{cart}')
def Quit():
    global f
    f=0
cart = list()
f = 1
while f == 1:
    print('''
    1. Add to your cart
    2. Remove from your cart
    3. Clear your cart
    4. Show items in your cart
    5. Quit program
    ''')
    choice = int(input('Select an option (1,2,3,4 or 5): '))
    if choice == 1:
        Add()
    elif choice == 2:
        Remove()
    elif choice == 3:
        clear()
    elif choice == 4:
        show()
    elif choice == 5:
        Quit()
print('exiting')