for i in range(-5, -20, -5):
	print(i)


#Looping through Tuple, List & string
lst = [1, 2, 3, 4, 5, True, False]
tup = (1, 2, 3, "hello", True)
s = "my string"

for i in range(len(tup)):
	print(tup[i])
for item in lst:
	print(item)

# enumerate() function 
for i, item in enumerate(s):
	print(i, item)


#break Keyword
x = [2, 3, 4 , 4, 5]
for num in x:
	if num == 4:
		break
	print(num)


#continue Keyword
for num in x:
	if num == 4:
		continue
	print(num)


#Nested for Loops in Nested-List
lst = [[1, 2], [3, 4], [5, 6]]

for i in range(len(lst)):
	interior_list = lst[i]
	for j in range(len(interior_list)):
		print(interior_list[j])


# pass keyword
for i in range(3):
	pass


#For-else statement
words = ("hello", "name", "this", "is", "word")
target = "name"

for word in words:
	if word == target:
		print("I found the word!")
		break
else:
	print("I didn't find the word")
