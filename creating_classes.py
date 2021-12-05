class Person:  # creating first class
	pass

p1 = Person()   # instantiating custom class
print(p1)
print(type(p1))  # <class '__main__.Person'>


class Person:   # __init__() method & taking a parameter 
	def __init__(self, x):   
		print(x)     

p1 = Person(2) # 2
p2 = Person(3)



class Person:     # Creating and Accessing Attributes
	def __init__(self, name, age):
		self.name = name 
		self.age = age

p1 = Person("Tim", 21)
p2 = Person("Bill", 40)

print(p1.name, p1.age) 

p1.new = "random"   # making a new attribute of p1
print(p1.new)



class Fruit:    # Class Example
	def __init__(self, name, calories):
		self.name = name
		self.calories = calories

a = Fruit("Apple", 100)
a.color = "Red"
