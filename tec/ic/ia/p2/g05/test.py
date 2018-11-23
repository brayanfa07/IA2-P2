array=[[0,1,0,1,0],[1,1,1,0,0],[1,1,0,0,1],[0,0,1,1,0],[1,1,1,1,1]]


def search_inside_matrix(number_to_search):
	extremity_visited = []
	row_size = len(array)
	column_size = len(array[0])
	if matrix_is_empty():
		print("Se pueden crear nuevos individuos desde cero")
	else:
		for i in range(row_size):
			for j in range(column_size):
				if array[i][j] == number_to_search:
					if is_extreme(array, i, j):  

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

	return 0


	
