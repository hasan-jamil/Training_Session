x = set()
y = {1, 2}

print(type(x))
print(type(y))

y = {1, 2, 3, 2, 4}
print(y)


#.add(), .remove(), .clear(), .len() functions
x = {1, 2, 3, 2, "hello", True, (1, 2)}

x.add(4)    # {1, 2, 3, 4, "hello", True, (1, 2)}
x.remove(2)    # {1, 3, 4, "hello", True, (1, 2)}
x.clear()
print(len(x))    # 0. Because the set is empty


#in Operator
x = {1, 2, 3}
contains = 1 in x
print(contains)


#.union() method
x = {1, 2}
y = {2, 3}

z = x.union(y)
q = x | y
print(q)
print(z)
print(x)


#.intersection() & .difference() methods
x = {1, 2, 3}
y = {1, 2, 4}
z = x.intersection(y)
z = x & y
print(z)

z = x.difference(y)
z = x - y
print(z)


#.symmetric_difference() method
x = {1, 2, 3}
y = {1, 2, 4}
z = x.symmetric_difference(y)
z = x ^ y
print(z)


#.update() , .difference_update() & .symmetric_difference_update()
x = {1, 2, 3}
y = {1, 2, 4}
x.update(y)
print(x)

q = {1, 2, 3}
q.difference_update(y)
print(q)

q = {1, 2, 3}
q.symmetric_difference_update(y)
print(q)


#subsets and Supersets
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
print(x.issubset(y))
print(y.issuperset(x))
print(x <= y)
print(y >= x)



#set example 
numbers = set()

while True:
	num = int(input("Numbers: "))
	if num in numbers:
		break
	numbers.add(num)
