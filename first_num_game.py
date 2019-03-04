import random

number = random.randint(1, 100)
over = False
# number = 7 # For debugging only
tries = 0
guesses = 0
invalid = 0

print("You get 10 tries to try and guess a number between 1 and 100.")
name = str(input("\nPlease enter your name: "))

while over is False:
	guess = (input("\nGuess the number: "))
	if guess.isdigit():
		tries += 1
		if tries > 9:
			guesses += 1
			print("\nSorry, " + name.title() + ', you took too many guesses. You guessed ' + str(guesses) + ' numbers and ' + str(invalid) + ' invalid characters to be exact.')
			over = True
		elif int(guess) > number:
			print('Your number is too high!')
			guesses += 1
		elif int(guess) == number:
			guesses += 1
			print("\nCongratulations, " + name.title() + '! You guessed the number in ' + str(guesses) + ' valid guesses!')
			over = True
		elif int(guess) < number:
			print('Your number is too low')
			guesses += 1
	else:
		print('INVALID: Please enter a number: ')
		invalid += 1

print('\nThank you for playing!')
