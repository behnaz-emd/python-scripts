import random
guess_number = random.randint(1, 10)
guess = None
while guess_number != guess:
    guess = int(input("Enter number between 1 and 10 : "))
    if guess < guess_number:
        print("Too low. ")
    elif guess > guess_number:
        print("Too hight. ")
print("You guessed the right number. ")