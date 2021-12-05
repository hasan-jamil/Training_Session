class Person:
	def __init__(self, name):
		self.name = name
		self._salary = 0. # _ considered as private attributes

	def set_salary(self, salary):
		if salary < 0:
			raise ValueError("Hey, this is invalid!")
		self._salary = salary

	def get_salary(self):
		return round(self._salary)

	salary = property(get_salary, set_salary)  # legacy properties


p = Person("Tim")

p.salary = 100.12
print(p.salary)



class Person:       # New properties
	def __init__(self, name):
		self.name = name 
		self._salary = 0

	@property
	def salary(self):   # getter
		return round(self._salary)

	@salary.setter    
	def salary(self, salary):
		if salary < 0:
			raise ValueError("Hey this is invalid")
		self._salary = salary

p = Person("Tim")
p.salary = 101.111
print(p.salary)



class Time:         # property Example 1
	def __init__(self, second):
		self._second = second

	@property
	def second(self):
		print("run")
		return self._second

	@second.setter
	def second(self, second):
		if second < 0 or second > 60:
			raise ValueError("Invalid!")
		self._second = second

t = Time(54)
t.second = 39
print(t.second)

