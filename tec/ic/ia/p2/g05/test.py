import random

array=[[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,1,0],[1,0,0,1,0]]
direction_array = ["vertical", "horizontal", "left-diagonal", "right-diagonal"]

"""
def search_inside_matrix(number_to_search):
	extremity_visited = []
	row_size = len(array)
	column_size = len(array[0])
	direction = ""
	if matrix_is_empty():
		print("Se pueden crear nuevos individuos desde cero")
	else:
		for i in range(row_size):
			for j in range(column_size):
				if array[i][j] == number_to_search:
					if is_extreme(array, i, j):
						if is_have_more_elements(number_to_search, array ,i ,j):
							if count_same_symbols(number_to_search, "left", array, i, j) > 0:
								count_same_symbols(number_to_search, "left", array, i, j)
							elif count_same_symbols(number_to_search, "right", array, i, j) > 0:
								count_same_symbols(number_to_search, "right", array, i, j)
							elif count_same_symbols(number_to_search, "down", array, i, j) > 0:
								count_same_symbols(number_to_search, "down", array, i, j)
							elif count_same_symbols(number_to_search, "down-left", array, i, j) > 0:
								count_same_symbols(number_to_search, "down-left", array, i, j)
							elif count_same_symbols(number_to_search, "down-right", array, i, j) > 0:
								count_same_symbols(number_to_search, "down-right", array, i, j)
						else:
							print("El elemento es único")
						#Agregar al arreglo de visitados
					else:
						print("")
"""

def matrix_is_empty():
	row_size = len(array)
	column_size = len(array[0])
	found = False
	for i in range(row_size):
		for j in range(column_size):
			if array[i][j] == 1 or array[i][j] == 2:
				found = True
	return found

def is_extreme(array, i, j):
	is_extreme_value = True
	if (i-1) >= 0:
		if array[i-1][j] == 0 or array[i][j] == 0:
			is_extreme_value = True
			print("Es extremo hacia arriba")
		elif array[i-1][j-1] == 0 or array[i-1][j+1] == 0:
			is_extreme_value = True
			print("Es extremo en diagonal")
		else:
			is_extreme_value = False
	return is_extreme_value

def is_have_more_elements(number_to_search, array, i, j):
	equal_symbol = False
	before_position = j-1
	after_position = j+1
	under_position = i+1
	if array[i][before_position] == number_to_search or array[i][after_position] == number_to_search:
		equal_symbol = True
	elif array[under_position][j] == number_to_search:
		equal_symbol = True
	elif array[under_position][before_position] == number_to_search or array[under_position][after_position] == number_to_search:
		equal_symbol = True
	else:
		equal_symbol = False
	return equal_symbol

def count_same_symbols(number_to_search, direction, array, i, j):
	equal_symbol = True
	before_position = j-1
	after_position = j+1
	under_position = i+1
	count_symbol = 0
	while equal_symbol != False:
		if direction == "left":
			if array[i][before_position] == number_to_search:
				equal_symbol = True
				before_position += 1
				count_symbol += 1
		elif direction == "right":		
			if array[i][after_position] == number_to_search:
				equal_symbol = True
				after_position += 1
				count_symbol += 1
		elif direction == "down":
			if array[under_position][j] == number_to_search:
				equal_symbol = True
				under_position += 1
				count_symbol += 1
		elif direction == "down-left":
			if array[under_position][before_position] == number_to_search:
				equal_symbol = True
				under_position += 1
				before_position += 1
				count_symbol += 1
		elif direction == "down-right":
			if array[under_position][after_position] == number_to_search:
				equal_symbol = True
				under_position += 1
				after_position += 1
				count_symbol += 1
		else:
			equal_symbol = False
	return count_symbol

def win_row(array, number_to_search):
	row_size = len(array)
	column_size = len(array[0])
	pos_in_row = 0
	pos_in_column = 0
	win_value = False
	while (pos_in_row < row_size):
		while (pos_in_column + 3) < column_size:
			if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row][pos_in_column +1] == number_to_search) and (array[pos_in_row][pos_in_column + 2] == number_to_search) and (array[pos_in_row][pos_in_column + 3] == number_to_search):
				win_value = True
				return win_value
			else:
				pos_in_column += 1
		pos_in_column = 0
		pos_in_row += 1
	return win_value

def win_column(array, number_to_search):
	row_size = len(array)
	column_size = len(array[0])
	pos_in_row = 0
	pos_in_column = 0
	win_value = False
	while pos_in_column < column_size:
		while (pos_in_row + 3 ) < row_size:
			if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row + 1][pos_in_column] == number_to_search) and (array[pos_in_row + 2][pos_in_column] == number_to_search) and (array[pos_in_row + 3][pos_in_column] == number_to_search):
				win_value = True
				return win_value
			else:
				pos_in_row += 1
		pos_in_row = 0
		pos_in_column += 1
	return win_value

def win_right_diagonal(array, number_to_search):
	row_size = len(array)
	column_size = len(array[0])
	pos_in_row = 0
	pos_in_column = 0
	win_value = False
	while (pos_in_column + 3) < column_size:
		while (pos_in_row + 3 ) < row_size:
			if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row + 1][pos_in_column + 1] == number_to_search) and (array[pos_in_row + 2][pos_in_column + 2] == number_to_search) and (array[pos_in_row + 3][pos_in_column + 3] == number_to_search):
				win_value = True
				return win_value
			else:
				pos_in_row += 1
		pos_in_row = 0
		pos_in_column += 1
	return win_value

def win_left_diagonal(array, number_to_search):
	row_size = len(array)
	column_size = len(array[0])
	pos_in_row = 0
	pos_in_column = 3
	win_value = False
	while (pos_in_row + 3) < row_size:
		while (pos_in_column < column_size):
			if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row + 1][pos_in_column - 1] == number_to_search) and (array[pos_in_row + 2][pos_in_column - 2] == number_to_search) and (array[pos_in_row + 3][pos_in_column - 3] == number_to_search):
				win_value = True
				return win_value
			else:
				pos_in_column += 1
		pos_in_column = 3
		pos_in_row += 1
	return win_value

def generate_individual_array():
	individual_array = []
	count = 0
	while count < 4:
		individual_array.append(random.randint(1,2))
		count += 1
	return individual_array

def generate_random_poblation():
	random_poblation = []
	count = 0
	while count < 10:
		individual = generate_individual_array()
		if individual not in random_poblation:
			random_poblation.append(individual)
			count += 1
	print(random_poblation)

def search_array(general_array, array_to_search):
	if array_to_search in general_array:
		print("True")
		return True
	else:
		return False

def random_number():
	value = random.randint(1,2)
	print(value)

array1 = [[1,2,3],[4,5,6]]

generate_random_poblation()