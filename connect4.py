class GeneticConnect4(object):
	"""docstring for GeneticConnect4"""
	def __init__(self):
		super(GeneticConnect4, self).__init__()
		self.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
		self.generation = "" #Insert and object of Generation(array)

	def insert_disc(self):
		self.print_grid()
		disc = eval(input("INSERTE DONDE VA A COLOCAR LA FICHA --> "))
		if disc > 0 and disc <= 7:	
			disc = disc - 1
			rows_count = len(self.array)
			columns_count = len(self.array[0])
			actualPosition = rows_count - 1
			inserted = False
			while actualPosition >= 0 :
				if self.array[actualPosition][disc] == 0 and inserted == False:
					self.array[actualPosition][disc] = 1
					inserted = True
				else:
					actualPosition -= 1
			return self.insert_disc()
		else:
			print("Posición equivocada")
			return self.insert_disc()

	def print_grid(self):
		rows_count = len(self.array)
		columns_count = len(self.array[0])
		print()
		for i in range(rows_count):
			row = ""
			for j in range(columns_count):
				if self.array[i][j] == 0:
					row = row + " "
				elif self.array[i][j] == 1:
					row = row + "1"
				else:
					row = row + "2"
			print("| " + row+ " |")
		print("|_________|") 
		print()
		return 0


new_game = GeneticConnect4()
new_game.insert_disc()