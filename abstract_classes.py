class AbstractGame:       # Abstract Class
	def start(self):
		while True:
			start = input("Would you like to play? ")
			if start.lower() == "yes":
				break

		self.play()

	def end(self):
		print("The game has ended")
		self.reset()

	def play(self):
		raise NotImplementedError("You must provide an implementation for play()")

	def reset(self):
		raise NotImplementedError("You must provide an implementation for reset() ")



class RandomGuesser(AbstractGame):
	def __init__(self, rounds):
		self.rounds = rounds
		self.round = 0

	def reset(self):
		self.round = 0

	def play(self):
		while self.round < self.rounds:
			self.round += 1

			print(f"Welcome to round {self.round}. Let's begin! ")
			random_num = random.randint(0, 10)    # generate random integers from import random
			while True:             
				guess = input("Enter a number between 1-10: ")
				if int(guess) == random_num:
					print("You got it!")
					break

		self.end()

game = RandomGuesser(1)
game.start()
