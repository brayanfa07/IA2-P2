#Class that create a new generation inside the Connect 4
class Generation(object):

	def __init__(self):
		super(Generation, self).__init__()
		self.initial_population = []
		return 0

	def mutation(self, population):
		row_size = len(population)
		column_size = len(population[0])
		mutated_population = []
		for i in range(row_size):
			position = random.randint(0, 3)
			if population[i][position] == 1:
				population[i][position] == 2:
			else:
				population[i][position] == 1:
			mutated_population.append(population[i])
		return mutated_population		


	def crossover(self, population):
		row_size = len(population)
		column_size = len(population[0])
		crossed_population = []
		all_crossed = False
		while all_crossed != True: 
			if row_size % 2 == 0:
				first_index = 0
				second_index = 1
				while second_index != (row_size - 1):
					temp_array = []
					array_to_insert = []
					array_to_insert.append(population[first_index])
					array_to_insert.append(population[second_index])
					temp_array.append(population[first_index][2:3])
					temp_array.append(population[second_index][2:3])
					array_to_insert[first_index][2:3] = temp_array[2:3]
					array_to_insert[second_index][2:3] = temp_array[0:1]
					first_index += 1
					second_index += 1
					crossed_population.append(array_to_insert[first_index])
					crossed_population.append(array_to_insert[second_index])
				all_crossed = True
			else:
				first_index = 0
				second_index = 1
				while first_index != (row_size - 1):
					if first_index == (row_size - 1):
						other_individual = random.randint(0, row_size - 2)
						temp_array = []
						array_to_insert = []
						array_to_insert.append(population[first_index])
						array_to_insert.append(population[other_individual])
						temp_array.append(population[first_index][2:3])
						temp_array.append(population[other_individual][2:3])
						array_to_insert[first_index][2:3] = temp_array[2:3]
						array_to_insert[other_individual][2:3] = temp_array[0:1]
						first_index += 1
						crossed_population.append(array_to_insert[first_index])
						crossed_population.append(array_to_insert[second_index])
					else:
						temp_array = []
						array_to_insert = []
						array_to_insert.append(population[first_index])
						array_to_insert.append(population[second_index])
						temp_array.append(population[first_index][2:3])
						temp_array.append(population[second_index][2:3])
						array_to_insert[first_index][2:3] = temp_array[2:3]
						array_to_insert[second_index][2:3] = temp_array[0:1]
						crossed_population.append(array_to_insert[first_index])
						crossed_population.append(array_to_insert[second_index])
						first_index += 1
						second_index += 1
				all_crossed = True
		return crossed_population

	def selection(self):
		#IMPLEMENT THE CODE
		return 0

	def fitness_funtion(self):
		#IMPLEMENT THE CODE	
		return 0

	def define_population(self, board_array):
		#IMPLEMENT THE CODE	
		return 0

	def search_inside_matrix(self, board_array):
		matrix_empty = False
		visited_array = []
		if is_empty_matrix()


