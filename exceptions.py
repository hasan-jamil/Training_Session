try:
	int("hello")
except:
	print("Exception")

print("Done")



#ValueError & ZeroDivisionError
try:
	int("hello")
except ValueError as e:
	print("Value Exception!", e)
except ZeroDivisionError as e:
	print("Zero Div Exception!", e)

print("Done")



#Handling General Exception
try:
	2 / 0
except Exception as e:
	print("Exception!", e)

print("Done")



#Finally Block
try:
	# 2 / 0
	int(1)
except Exception as e:
	print("Exception!", e)
finally:
	print("Done")



#Raising Exceptions
#raise Exception("this is an error")



#Exception Example 1
num = input("Enter a number: ")

if not num.isdigit():
	raise ValueError("This is not a valid number!")



#Exception Example 2
while True:
	num = input("Enter a number: ")

	try:
		num = float(num)
		break
	except ValueError:
		print("Not a valid float, try again!")
