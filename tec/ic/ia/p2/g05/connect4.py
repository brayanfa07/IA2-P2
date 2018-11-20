
#Class that implements the structure of the Connect4
class GeneticConnect4(object):

	#Init the main structure
	def __init__(self):
		super(GeneticConnect4, self).__init__()
		self.board_array = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
		self.generation = "" #Insert and object of Generation(board_array)

	#Function that insert a disc inside the board
	def insert_disc(self):
		self.print_board()
		disc = eval(input("INSERTE DONDE VA A COLOCAR LA FICHA --> "))
		if disc > 0 and disc <= 7:	
			disc = disc - 1
			rows_count = len(self.board_array)
			columns_count = len(self.board_array[0])
			actual_position = rows_count - 1
			inserted = False
			while actual_position >= 0 :
				if self.board_array[actual_position][disc] == 0 and inserted == False:
					self.board_array[actual_position][disc] = 1
					inserted = True
				else:
					actual_position -= 1
			return self.insert_disc()
		else:
			print("Posición equivocada")
			return self.insert_disc()

	#Function that print the board
	def print_board(self):
		rows_count = len(self.board_array)
		columns_count = len(self.board_array[0])
		print()
		for i in range(rows_count):
			row = ""
			for j in range(columns_count):
				if self.board_array[i][j] == 0:
					row = row + " "
				elif self.board_array[i][j] == 1:
					row = row + "1"
				else:
					row = row + "2"
			print("| " + row+ " |")
		print("|_________|") 
		print()
		return 0