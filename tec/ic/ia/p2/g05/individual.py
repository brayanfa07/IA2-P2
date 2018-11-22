class Individual(object):
	"""docstring for Individual"""
	def __init__(self, arg):
		super(Individual, self).__init__()
		self.disc_array = []
		self.player_disc_initial_count = 0
		self.fitness_value = 0

	def set_disc_array(self, array):
		self.disc_array = array
		return 0

	def set_fitness_value(self):
		number_of_disc = 0
		fitness_value = 0
		while fitness_value <= 100:
			if self.player_disc_initial_count == number_of_disc:
				self.fitness_value = 0
				break
			else:
				number_of_disc += 1
				fitness_value += 25
		return fitness_value



