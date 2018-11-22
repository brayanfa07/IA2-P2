import os
from generation import Generacion

#Class that implements the structure of the Connect4
class GeneticConnect4(object):

	#Init the main structure
	def __init__(self):
		super(GeneticConnect4, self).__init__()
		self.board_array = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
		self.generation = "" #Insert and object of Generation(board_array)
		self.player_one = ""
		self.player_two = ""
		return self.main_menu()

	def set_player(self, player_one, player_two):
		self.player_one = player_one
		self.player_two = player_two
		return 0

	def main_menu(self):
		print("**********************		CONNECT 4 GENÉTICO		**********************")
		print()
		print("		Tipos de juego: ")
		print("		1. HUMANO - MÁQUINA")
		print("		2. MÁQUINA - MÁQUINA")
		print("")
		game_type = input("Defina el tipo de juego seleccionando un número de opción --> ")
		if game_type == "1":
			self.set_player("HUMANO", "MÁQUINA")
		elif game_type == "2":
			self.set_player("MÁQUINA 1", "MÁQUINA 2")
		else:
			print("Ingrese una opción correcta")
			input("Presione una tecla para continuar --> ")
			os.system('clear')
			return self.main_menu()
		return self.insert_disc(self.player_one)
			
	#Function that insert a disc inside the board
	def insert_disc(self, player):
		print()
		print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
		print()
		self.print_board()
		print()
		print("JUGADOR: " + player)
		disc_type = 0
		actual_player = ""
		next_player = "" 
		try:
			position = eval(input("ELIJA LA COLUMNA A COLOCAR LA FICHA, DEL 1 AL 7 --> "))
			if player == "HUMANO" or player == "MÁQUINA 1":
				disc_type = 1
				next_player = self.player_two
				actual_player = self.player_one
			else:
				disc_type = 2
				next_player = self.player_one
				actual_player = self.player_two
			if position > 0 and position <= 7:
				position = position - 1
				rows_count = len(self.board_array)
				columns_count = len(self.board_array[0])
				actual_position = rows_count - 1
				inserted = False
				while actual_position >= 0 :
					if self.board_array[actual_position][position] == 0 and inserted == False:
						self.board_array[actual_position][position] = disc_type
						inserted = True
					else:
						actual_position -= 1
				return self.insert_disc(next_player)
			else:
				print("Posición equivocada")
				input("Presione una tecla para continuar --> ")
				return self.insert_disc(actual_player)
		except Exception as e:
			print("Posición equivocada")
			input("Presione una tecla para continuar --> ")
			return self.insert_disc(actual_player)


	#Function that print the board
	def print_board(self):
		os.system('clear')
		rows_count = len(self.board_array)
		columns_count = len(self.board_array[0])
		print()
		for i in range(rows_count):
			row = ""
			for j in range(columns_count):
				if self.board_array[i][j] == 0:
					row = row + " "
				elif self.board_array[i][j] == 1:
					row = row + "X"
				else:
					row = row + "O"
			print("| " + row + " |")
		print("|_________|") 
		print()
		return 0