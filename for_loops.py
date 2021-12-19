for i in range(-5, -20, -5):
	print(i)

                       
lst = [1, 2, 3, 4, 5, True, False]  # Looping through Tuple, List & string
tup = (1, 2, 3, "hello", True)
s = "my string"

for i in range(len(tup)):
	print(tup[i])
for item in lst:
	print(item)


for i, item in enumerate(s):   # enumerate() function 
	print(i, item)



x = [2, 3, 4 , 4, 5] # break Keyword
for num in x:
	if num == 4:
		break
	print(num)



for num in x:     # continue Keyword
	if num == 4:
		continue
	print(num)



lst = [[1, 2], [3, 4], [5, 6]]   # Nested for Loops in Nested-List

for i in range(len(lst)):
	interior_list = lst[i]
	for j in range(len(interior_list)):
		print(interior_list[j])



for i in range(3):   # pass keyword
	pass


words = ("hello", "name", "this", "is", "word")    # For-else statement
target = "name"

for word in words:
	if word == target:
		print("I found the word!")
		break
else:
	print("I didn't find the word")
