number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
	print("This is a positive even number")

	number2 = int(input("Number: "))
	if number2 < 0:
		print("This is a negative Number")
	else:
		print("This is a positive Number")
else:
	print("not a good job")