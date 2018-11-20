array = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


class GeneticConnect4(object):
	"""docstring for GeneticConnect4"""
	def __init__(self):
		super(GeneticConnect4, self).__init__()
		self.arg = arg

	def mutation():
		return 0		


	def crossing():
		return 0


	def 


	def 
def insert_disc():

	print_grid(array)

	disc = eval(input("INSERTE DONDE VA A COLOCAR LA FICHA --> "))

	if disc > 0 and disc <= 7:	
		disc = disc - 1

		rowsCount = len(array)
		columnsCount = len(array[0])

		actualPosition = rowsCount - 1
		inserted = False

		while actualPosition >= 0 :
			if array[actualPosition][disc] == 0 and inserted == False:
				array[actualPosition][disc] = 1
				inserted = True
			else:
				actualPosition -= 1
		return insert_disc()
	else:
		print("Posición equivocada")
		return insert_disc()


def print_grid(array):

	rowsCount = len(array)
	columnsCount = len(array[0])

	print()
	for i in range(rowsCount):
		row = ""
		for j in range(columnsCount):
			if array[i][j] == 0:
				row = row + " "
			elif array[i][j] == 1:
				row = row + "1"
			else:
				row = row + "2"
		print("| " + row+ " |")

	print("|_________|") 
	print()

	return 0

insert_disc() 