# -*- coding: utf-8 -*-
"""
Challenge #1: Build a guessing game. You defined a secrect number and
the player has 5 times to guess it from keyboard. If the guess is correct, 
print "Congratulation. You win 1 million dollar!" and stop the loop. Else 
print "Incorrect number. Try again" and repeat the guess. After 5 incorrect 
guess stop the loop and print "You failed. Better luck next time."
"""

secret_number = 9
guess_count = 0
guess_limit = 5

#  While Loop
""" 
while guess_count < guess_limit:
    guess = int(input("Show me your number: "))
    if guess == secret_number:
        print("You win 1 million dollar !!!!!!! ")
        break
    elif guess_count <4:
        print("Incrrect number. Try again")   
    else:
        print("You failed. Better luck next time")
    guess_count +=1
"""    

# For Loop
for guess_count in range(guess_limit):
    guess = int(input("Show me your number: "))
    if guess == secret_number:
        print("You win 1 million dollar")
        break
    elif guess_count <4:
        print("Incrrect number. Try again")   
    else:
        print("You failed. Better luck next time")