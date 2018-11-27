from g05.generation import Generation
from random import Random
import pytest 

new_generation = None
board_array = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

@pytest.fixture
def setup_class():
	global new_generation
	new_generation = Generation(board_array, 1)

def test_mutation(setup_class):
	rando = Random(777)	
	population = [[1,1,2,1],[2,2,1,2],[1,2,1,2],[2,1,2,1],[1,1,2,2],[2,2,1,1],[1,2,2,2],[2,1,1,1],[2,2,2,1],[1,1,1,1]]
	mutated_population = new_generation.mutation(population)
	test_population = []
	for i in range(10):
		position = rando.randint(0, 3)
		if population[i][position] == 1:
			population[i][position] = 2
		else:
			population[i][position] = 1
		test_population.append(population[i])
	assert mutated_population == test_population

def test_calculate_consecutive(setup_class):
	individual = [1,1,1,2]
	value = new_generation.calculate_consecutive(individual, 1)
	assert value == 3

def test_fitness_funtion(setup_class):
	individual = [1,1,1,2]
	value = new_generation.fitness_funtion(individual, 1)
	assert value == 75

def test_matrix_is_empty(setup_class):
	value = new_generation.matrix_is_empty()
	assert value == True

def test_is_extreme(setup_class):
	value = new_generation.is_extreme(board_array, 0, 0)
	assert value == True

def test_is_have_more_elements(setup_class):
	value = new_generation.is_have_more_elements(0, board_array, 5, 4)
	assert value == True

def test_win_row(setup_class):
	value = new_generation.win_row(board_array, 2)
	assert value == False

def test_win_column(setup_class):
	value = new_generation.win_column(board_array, 1)
	assert value == False

def test_win_right_diagonal(setup_class):
	value = new_generation.win_right_diagonal(board_array, 1)
	assert value == False

def test_win_left_diagonal(setup_class):
	value = new_generation.win_left_diagonal(board_array, 1)
	assert value == False

def test_generate_individual_array(setup_class):
	test_array = []
	rando = Random(777)
	count = 0
	while count < 4:
		test_array.append(rando.randint(1, 2))
		count += 1
	value = new_generation.generate_individual_array()
	assert value == test_array

def test_search_array(setup_class):
	array = [0, 0, 0, 0, 0, 0, 0]
	value = new_generation.search_array(board_array, array)
	assert value == True

def test_random_direction(setup_class):
	direction_array = ["vertical", "horizontal"]
	rando = Random(777)
	index = rando.randint(0, 1)
	value = new_generation.random_direction()
	assert value == direction_array[index]

def test_random_number(setup_class):
	rando = Random(777)
	numb = rando.randint(1,2)
	value = new_generation.random_number()
	assert value == numb