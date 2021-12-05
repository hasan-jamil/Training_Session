class Person:        # Super/ Base / Parent Class 
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def say_hello(self):
		print(f"Hi my name is {self.first_name} {self.last_name}")


class Employee(Person):    # Sub / Derived / Child Class
	def test(self):
		print("test")

e = Employee("Tim", "Programmer")
e.say_hello()
e.test()



class Employee(Person):
	def say_hello(self):
		print("---")
		super().say_hello()    # Overriding Method with super()
		print("---")

e = Employee("Tim", "Programmer")
e.say_hello()



class Employee(Person):
	def __init__(self, first_name, last_name, salary):  # Overriding the Constructor
		super().__init__(first_name, last_name)
		self.salary = salary

	def say_hello(self):
		super().say_hello()      # Overriding Method
		print(f"My salary is {self.salary}")

e = Employee("Tim", "Programmer", 50000)
e.say_hello()



class Manager(Employee):        # inheritance hierarchies
	def __init__(self, first_name, last_name, salary, department):
		super().__init__(first_name, last_name, salary)
		self.department = department

m = Manager("Tim", "Programmer", 50000, "Sports")
m.say_hello()



class Owner(Person):
	def __init__(self, first_name, last_name, net_worth):
		super().__init__(first_name, last_name)
		self.net_worth = net_worth

o = Owner("Tim", "Programmer", 50000)
o.say_hello()

print(isinstance(o, Person))     # True



class A:       # Multiple Inheritance 
	pass

class B:
	def __init__(self):
		print("B")

class C(A, B):
	def __init__(self):
		super().__init__()

c = C()  # B  



class Duck:      # Duck Typing 
	def swim(self):
		print("Swimming Duck")

	def fly(self):
		print("Flying Duck")

class Whale:
	def swim(self):
		print("Swimming Whale")

animals = [Duck(), Duck(), Whale()]

for animal in animals:
	animal.swim()
	animal.fly()
