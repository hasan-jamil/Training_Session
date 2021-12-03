def print_value(value):
	print(value)

print_value("hello")


#Multiple function parameters 
def add_5(x, y, z):
	result = x + y + z + 5
	print(result)

add_5(5, 5, 2)



#return Values
def get_negative_sum(x, y, z):
	result = x + y + z
	if result < 0:
		return result

	return 1
r = get_negative_sum(5, 6, 13)
print(r)


# Optional/Default Parameters
def new_range(start=0, stop=10):
	x = start

	while x < stop:
		print(x)
		x += 1
new_range()
new_range(stop=5, start=2)


# Returning multiple values
def return_values(x, y):
	return x + 1, y + 1

x, y = return_values(5, 6)
print(x, y)


#Function Example 1
def remove_chars(base, chars):
	new_string = base
	for char in chars:
		new_string = new_string.replace(char, "")
	return new_string

result = remove_chars("hello world", "l")
print(result)



#Function Example 2 & Nested function
def sum_lists(list1, list2):
	def sum_list(lst):
		total = 0
		for num in lst:
			total += num
		return total

	list1_sum = sum_list(list1)
	list2_sum = sum_list(list2)
	return list1_sum, list2_sum


sum1, sum2 = sum_lists(list1=[1, 2, 3, 4], list2=[-1, -2, -3, -4])
print(sum1, sum2)
