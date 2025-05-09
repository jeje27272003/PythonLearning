#GuessNumberGame
import random
import os
import platform


def clear_screen():
	# Clear the screen based on the operating system
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

print("Welcome to the Guess Number Game!")
print("please choose a difficulty for the game")
print("1. Easy (1-100)")
print("2. Medium (1-1000)")
print("3. Hard (1-10000)")

while True:
	try:
		difficulty = int(input("Enter the difficulty level (1-3): "))
		if difficulty in [1, 2, 3]:
			break
		else:
			print("Invalid input. Please enter a number between 1 and 3.")
	except ValueError:
		print("Invalid input. Please enter a number for the difficulty level.")

if difficulty == 1:
	guessmax = 100
	number_to_guess = random.randint(1, 100)
elif difficulty == 2:
	guessmax = 1000
	number_to_guess = random.randint(1, 1000)
else:
	guessmax = 10000
	number_to_guess = random.randint(1, 10000)

clear_screen()
print(f"\nYou have chosen difficulty level {difficulty}.")
attempts = 0
guessmin = 1
guesslist = []
while True:
	try:
		print(f"Guess a number between {guessmin} and {guessmax}.")
		print(f"You have made {attempts} attempts.")
		if attempts > 0:
			print(f"you've guessed {guesslist} before")
		guess = int(input("Enter your guess: "))
		if guess > number_to_guess and guess < guessmax:
			clear_screen()
			print("Too high! Try again.")
			attempts += 1
			guessmax = guess
			guesslist.append(guess)
		elif guess < number_to_guess and guess > guessmin:
			clear_screen()
			print("Too low! Try again.")
			attempts += 1
			guessmin = guess
			guesslist.append(guess)
		elif guess == number_to_guess:
			clear_screen()
			attempts += 1
			guesslist.append(guess)
			print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
			break
		else:
			clear_screen()
			print(f"Invalid input. Please enter a number between 1 and {guessmax}.")
	except ValueError:
		print("Invalid input. Please enter a number for your guess.")