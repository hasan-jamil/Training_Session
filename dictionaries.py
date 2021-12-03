x = {2 : "hello", "1" : 5}
print(x["1"])


#Adding Keys
y = {}
x = dict()
y["key"] = "value"
print(y)
print(x)


#Deleting Keys
x = {1: 1, 2: 2, 3: 3}
del x[1]
print(x)


#in Operator
x = {1: 1, 2: 2, 3: 3}
contains = 1 in x
print(contains)


#.values(), .keys(), .items(), .len() Functions
x = {1: 1, 2: 2, 3: 3}
values = x.values()
keys = list(x.keys())
items = x.items()
print(values)
print(keys[0])
print(items)
print(len(x))


#Looping through a Dictionary
x = {2: 1, 3: 3}

for key in x:
	value = x[key]
	print(key, value)

for key, value in x.items():
	print(key, value)


#.get() function
x = {2: 1, 3: 3}
x[4] = x.get(4, 2) + 1
print(x)


#Dictionary Example-1
characters = {}
string = "hello world"
for char in string:
	characters[char] = characters.get(char, 0) + 1;
print(characters)


#Dictionary Example-2
counts = {}

while True:
	num = input("Number (enter q to quit): ")
	if num == "q":
		break
	num = int(num)
	counts[num] = counts.get(num, 0) + 1
print(counts)
