import sys

calc = 0

number = input("Enter first number: ")
sign = input("Enter symbol you need (+,-,*,/): ")
number2 = input("Enter second number: ")

if(sign == '+'):
	calc = int(number) + int(number2)
	print(number + '+' + number2)

if(sign == '-'):
	calc = int(number) - int(number2)
	print(number + '-' + number2)

if(sign == '*'):
	calc = int(number) * int(number2)
	print(number + '*' + number2)

if(sign == '/'):
	calc = int(number) / int(number2)
	print(number + '/' + number2)

print(calc)