# 1) user input => low and high bound
# 2) random => [a, b]
# 3)loop => condition => guess_count=5 
import random

try:
    low = int(input("Enter the low bound: \n"))
    high = int(input("Enter the high bound: \n"))
except:
    print("Invalid input. Please enter valid integers.")
    exit()

random_number = random.randint(low, high)

guess_count = 5
while guess_count > 0:
    user_guess = int(input(f"Enter your guess ({guess_count} attempts left): \n"))
    if user_guess == random_number:
        print("Congratulations! You've guessed the number.")
        break
    elif user_guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    guess_count -= 1

if guess_count == 0:
    print(f"Sorry, you've run out of guesses. The number was {random_number}.")
    print("Game Over")
    print("Thank you for playing!")
    print("Goodbye!")

