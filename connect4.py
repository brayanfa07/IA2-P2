array = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1]]

def insert_disc():

	print_grid(array)

	disc = eval(input("INSERTE DONDE VA A COLOCAR LA FICHA --> "))
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


def print_grid(array):

	rowsCount = len(array)
	columnsCount = len(array[0])

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

	return 0

insert_disc()