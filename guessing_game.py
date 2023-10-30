import random

# Generate a random number between 0 and 10
number_to_guess = random.randint(0, 10)
while True:
    # Prompt the user to guess the number
    user_guess = int(input("Guess the number between 0 and 10: "))
        # If the user guessed wrong, tell them if their guess was too high or too low
    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else: # Check if the user guessed correctly
         print("Congratulations! You've guessed the number.")
    break    

