class Person:
	def __init__(self, name):
		self.name = name
		self.age = None 

	def say_hello(self):     # Creating a method
		print(f"Hello, {self.name}")

	def set_age(self, age):  # setter method
		self.age = age

	def get_age(self):   #getter method
		return self.age

p1 = Person("Tim")
p1.say_hello()

p1.set_age(21)
print(p1.age)
print(p1.get_age())



class Counter:        # Method example 1
	def __init__(self):
		self.count = 0
		self.locked = False

	def toggle_lock(self):
		self.locked = not self.locked

	def increment(self):
		if self.locked:
			raise Exception("The counter is locked!")
		self.count += 1

	def decrement(self):
		if self.locked:
			raise Exception("The counter is locked!")
		self.count -= 1

	def print_count(self):
		print(f"The current count is {self.count} ")


counter = Counter()
counter.decrement()
counter.print_count()

counter.toggle_lock()
counter.increment()
