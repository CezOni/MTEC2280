import sys

print("Hello, world!")
print("Guess the # from 1 through 10") 

number = input('Enter your guess: ')

sys.argv[0] = number

guess = sys.argv[0]
answer = 9

intGuess = int(guess)

if(intGuess == answer):
	print("You won!")

if(intGuess != answer):
	print("Sorry that is incorrect. You lose.")