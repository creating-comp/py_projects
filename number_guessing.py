'''
Build a Number guessing game, in which the user selects a range.+
Let’s say User selected a range, i.e., from A to B,+
where A and B belong to Integer.+
Some random integer will be selected by the system and+
the user has to guess that integer in the minimum number of guesses+
'''
from random import randint
a = int(input("Your range is from: "))
b = int(input("To: "))
value = randint(a, b)
count = 0
guess = ""
while(guess!=value):
    guess = int(input("Guess an integer in this range: "))
    if guess < value:
        print("Try again. You guessed too small.", end=" ")
        count += 1
        print(f"That's your {count}. guess")
        if count == 3:
            print("Game over. You are out of guesses.")
            break
    elif guess > value:
        print("Try again. You guessed too large.", end=" ")
        count += 1
        print(f"That's your {count}. guess")
        if count == 3:
            print("Game over. You are out of guesses.")
            break
if guess==value:
    print(f"You win, congrats. It was your {count+1}.try")