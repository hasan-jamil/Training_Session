x = 0
while x < 5:
	print(x)
	x += 1


#break keyword 
while True:
	num = input("Enter an integer: ")
	if num.isdigit():
		break


#Looping through a List
lst = [2, 3, 3, -2, -2, -1]

result = 0
i = 0

while result < 9 and i < len(lst):
	num = lst[i]
	result += num
	i += 1
	print(num)


#while-else statement
lst = [2, 3, 3,  -1]
i = 0

while i < len(lst):
	if lst[i] == -2:
		print("Found it!")
		break
	i += 1
else:
	print("Didn't find it")
