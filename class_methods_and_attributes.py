class Car:
	number_of_cars = 0    # Class Attributes

	def __init__(self, make, model):
		self.make = make
		self.model = model
		Car.number_of_cars += 1

	@classmethod         # Class Method
	def update_number_of_cars(cls, cars):
		cls.number_of_cars = cars
		print("run")





c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

print(c1.number_of_cars)  # 2 

Car.update_number_of_cars(10)

print(c2.number_of_cars)   # 10
print(Car.number_of_cars)  # 10


class Circle:      # Class Methods And Attributes Example 1
	pi = 3.14

	@classmethod
	def area(cls, radius):
		return cls.pi * (radius ** 2)

	@classmethod
	def perimeter(cls, radius):
		return 2 * cls.pi * radius

	@classmethod
	def get_area_and_perimeter(cls, radius):
		return cls.area(radius), cls.perimeter(radius)


print(Circle.get_area_and_perimeter(4))
