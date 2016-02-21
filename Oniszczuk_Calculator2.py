import sys

calc = 0

number = raw_input("Enter first number: ")
sign = raw_input("Enter symbol you need (+,-,*,/): ")
number2 = raw_input("Enter second number: ")

if(sign == '+'):
	calc = int(number) + int(number2)
	print(number + '+' + number2)

if(sign == '-'):
	calc = int(number) - int(number2)
	print(number + '-' + number2)

if(sign == '*'):
	calc = int(number) + int(number2)
	print(number + '*' + number2)

if(sign == '/'):
	calc = int(number) + int(number2)
	print(number + '/' + number2)

print(calc)