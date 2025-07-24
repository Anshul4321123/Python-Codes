import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess == number:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

while True:
    b = input("Rate the game from 1 to 5: ")
    if b.isdigit():
        b = int(b)
        if b < 0:
            print("You are not allowed to give a negative rating.")
        elif b > 5:
            print("Thank you, but those are too many stars for us to handle!")
        else:
            print("Thank you for your rating!")
            break
    else:
        print("Please enter a valid number from 1 to 5.")
