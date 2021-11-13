import random
print('NUMBER GUESSING GAME')
print('Guess a Number (0-9)')
number=random. randint(0,9)
guess=input('Enter the Number here : ')
if number==guess :
    print('You Win!!')
else :
    print('YOU LOOSE! The number is',number)