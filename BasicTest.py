from datetime import datetime
import time
username = input("Enter your username: ")
lives = 10
def checkLives():
    if lives <= 0:
        print('Sorry, but you are out of lives.')
        print('Exiting the program...\n')
        time.sleep(3)
        quit()
    else:
        pass

print(f"Greetings, {username}!")
time.sleep(1)
print("The goal is to answer 12 questions you are going to be given, spent as little time as possible and save all of your 10 lives!")
time.sleep(3.5)
print("Start the game by typing 'GO'. Good Luck!")

while True:
    CONFIRMATION = str(input())
    CONFIRMATION = CONFIRMATION.lower()
    if CONFIRMATION == 'go':
        break 
    else:
        print('Not ready...? No problem, take your time.')
start_time = time.time()

# Question 1
print('Q1:  10x - 100 = 20;    x = ', end = "")
ans = 12
response = int()
try:
    response = int(input())
except:
    print('The answer is an INTEGER.') 
if response == ans:
    print('Correct! Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

# Question 2
print('Q2:  x^2 = 144;    x = ', end = "")
ans = 12
try:
    response = int(input())
except:
    print('The answer is an INTEGER.') 
if response == ans:
    print('Good! Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

# Question 3
print('Q3:  Sally is 54 years old and her mother is 80, how many years ago was Sally’s mother times her age?;    x = ', end = "")
ans = 41
try:
    response = int(input())
except:
    print('The answer is an INTEGER.') 
if response == ans:
    print('Awesome! Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

# Question 4
print('Q4:  Which country has the highest population?    Your answer: ', end = "")
ans = 'china'
response = str(input())
if response == ans:
    print('Right! Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

#Question 5
print('Q5:  What heats the water in a hot spring?    Your answer: ', end = "")
ans = 'magma'
response = str(input())
if response == ans:
    print('Right. Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

#Question 6
print('Q6:  Bacterial infections in humans can be treated with what?    Your answer: ', end = "")
ans = ['antibiotics', 'antibiotic']
response = str(input())
if response == ans:
    print('Well done. Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

#Question 7
print('Q7:  Which is the largest island in the world?    Your answer: ', end = "")
ans = 'greenland'
response = str(input())
if response == ans:
    print('Correct. Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

#Question 8
print('Q8:  Can frogs live in salt water?    Your answer(y/n): ', end = "")
ans = 'y'
response = str(input())
if response == ans:
    print('Correct. Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

#Question 9
print('Q9:  Can you light a diamond on fire?    Your answer(y/n): ', end = "")
ans = 'y'
response = str(input())
response = response.lower()
if response == ans:
    print('Correct. Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')

#Question 10
print('Q10:  When did Columbus discover the Americas?    Your answer: ', end = "")
ans = '1492'
try:
    response = str(input())
except:
    print('The answer is an INTEGER - an year')
if response == ans:
    print('Awesome! Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')
checkLives()

#Question 11
print('Q11:  -x + 3(2x+5) = 100   x = ', end = "")
ans = 17
response = str(input())
if response == ans:
    print('Correct. Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')
checkLives()

#Question 12
print('Q12:  Whats the fifth planet from the sun?    Your answer: ', end = "")
ans = 'jupiter'
response = str(input())
response = response.lower()
if response == ans:
    print('Correct. Keep going.\n')
else:
    lives-=1
    print(f'Wrong. Current lives: {lives}\n')
checkLives()
res_time = time.time() - start_time
res_time = round(res_time, 2)
print(f'Congratulations, you passed the test in about {res_time} seconds :)\n')






