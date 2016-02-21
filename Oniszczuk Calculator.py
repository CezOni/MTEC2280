import sys

number = sys.argv[1]
sign = sys.argv[2]
number 2 = sys.argv[3]
calc = 0

print(type(number))
print(type(sign))
print(type(number2))

number = input("Enter first number: ")
sign = input("Enter the symbol you need (+,-,*,/): ")
number2 = input("Enter second number: ")

if(sign == '+')
	calc = int(number) + int(number2)
	print(number + '+' + number2)

if(sign == '-')
	calc = int(number) - int(number2)
	print(number + '-' + number2)

if(sign == '*')
	calc = int(number) + int(number2)
	print(number + '*' + number 2)

if(sign == '/')
	calc = int(number) + int(number2)
	print(number + '/' + number2)

print calc