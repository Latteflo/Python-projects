import random

number_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

user_guess= None 

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))
    difference = abs(number_to_guess - user_guess)
    if difference == 0:
        print("Congratulations! You guessed the correct number!")
    elif difference <= 5:
        print("Very close! Try again.")
    elif difference <= 10:
        print("Close! Try again.")
    else:
        print("Far off. Try again.")