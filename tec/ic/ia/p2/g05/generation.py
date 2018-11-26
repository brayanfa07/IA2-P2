import random

TOTAL_GENERATIONS = 10
INDIVUALS_NEXT_GENERATION = 10

# Class that create a new generation inside the Connect 4


class Generation:

    def __init__(self, board_array, disc_type):
        super(Generation, self).__init__()
        self.initial_population = []
        self.array = board_array
        self.direction_array = [
            "vertical", "horizontal",
            "left-diagonal", "right-diagonal"
        ]
        self.disc_type = disc_type
        return None

    def mutation(self, population):
        row_size = len(population)
        column_size = len(population[0])
        mutated_population = []
        for i in range(row_size):
            position = random.randint(0, 3)
            if population[i][position] == 1:
                population[i][position] == 2
            else:
                population[i][position] == 1
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
                        array_to_insert[other_individual][
                            2:3] = temp_array[0:1]
                        first_index += 1
                        crossed_population.append(array_to_insert[first_index])
                        crossed_population.append(
                            array_to_insert[second_index])
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
                        crossed_population.append(
                            array_to_insert[second_index])
                        first_index += 1
                        second_index += 1
                all_crossed = True
        return crossed_population

    def selection(self, population):
        return 0

    def fitness_funtion(self, individual_array, disc_type):
        row_size = len(individual_array)
        function_value = 0
        consecutive_value = calculate_consecutive(individual_array, disc_type)
        if consecutive_value == 1:
        	function_value = 25
        elif consecutive_value == 2:
        	function_value = 50
       	elif consecutive_value == 3:
       		function_value = 75
       	elif consecutive_value == 4:
       		function_value = 100
       	else:
       		function_value = 0
        return function_value



    def calculate_consecutive(self, individual_array, disc_type):
    	consecutive_value = 0
    	if individual_array[0] == disc_type and individual_array[1] == disc_type and individual_array[2] == disc_type and individual_array[3] == disc_type:
    		return consecutive_value = 4
    	elif (individual_array[0] == disc_type and individual_array[1] == disc_type and individual_array[2] == disc_type) or (individual_array[1] == disc_type and individual_array[2] == disc_type and individual_array[3] == disc_type):
    		return consecutive_value = 3
    	elif (individual_array[0] == disc_type and individual_array[1] == disc_type) or (individual_array[1] == disc_type and individual_array[2] == disc_type) or (individual_array[02] == disc_type and individual_array[3] == disc_type):
    		return consecutive_value = 2
    	elif (individual_array[0] == disc_type) or (individual_array[1] == disc_type) or (individual_array[2] == disc_type) or (individual_array[3] == disc_type):
    		return consecutive_value = 1

    def define_population(self, board_array):
        # IMPLEMENT THE CODE
        return 0

    #REVISADO
    def matrix_is_empty(self):
        row_size = len(self.array)
        column_size = len(self.array[0])
        found = True
        for i in range(row_size):
            for j in range(column_size):
                if self.array[i][j] == 1 or self.array[i][j] == 2:
                    found = False
        return found

    #Revisado
    def is_extreme(self, array, i, j):
        is_extreme_value = True
        if (i - 1) >= 0 and j < len(array[0]):                
            print(i, " i1")
            print(j, " j1")
            if array[i - 1][j] == 0:
                is_extreme_value = True
                print(i, " i2")
                print(j, " j2")
                print("Es extremo hacia arriba")
            elif array[i - 1][j - 1] == 0 or array[i - 1][j + 1] == 0:
                is_extreme_value = True
                print(i, " i3")
                print(j, " j3")
                print("Es extremo en diagonal")
            else:
                is_extreme_value = False
        return is_extreme_value

    def is_have_more_elements(self, number_to_search, array, i, j):
        equal_symbol = False
        before_position = j - 1
        after_position = j + 1
        under_position = i + 1
        if (array[i][before_position] == number_to_search or
                array[i][after_position] == number_to_search):
            equal_symbol = True
        elif (array[under_position][j] == number_to_search):
            equal_symbol = True
        elif (array[under_position][before_position] == number_to_search or
                array[under_position][after_position] == number_to_search):
            equal_symbol = True
        else:
            equal_symbol = False
        return equal_symbol

    def count_same_symbols(self, number_to_search,
                           direction, array, i, j):
        equal_symbol = True
        before_position = j - 1
        after_position = j + 1
        under_position = i + 1
        count_symbol = 0
        while equal_symbol:
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

    #Revisado
    def win_row(self, array, number_to_search):
        row_size = len(array)
        column_size = len(array[0])
        pos_in_row = 0
        pos_in_column = 0
        win_value = False
        while (pos_in_row < row_size):
            while (pos_in_column + 3) < column_size:
                if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row][pos_in_column +
                        1] == number_to_search) and (array[pos_in_row][pos_in_column +
                        2] == number_to_search) and (array[pos_in_row][pos_in_column +
                        3] == number_to_search):
                    win_value = True
                    return win_value
                else:
                    pos_in_column += 1
            pos_in_column = 0
            pos_in_row += 1
        return win_value

    #Revisado
    def win_column(self, array, number_to_search):
        row_size = len(array)
        column_size = len(array[0])
        pos_in_row = 0
        pos_in_column = 0
        win_value = False
        while pos_in_column < column_size:
            while (pos_in_row + 3) < row_size:
                if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row +
                        1][pos_in_column] == number_to_search) and (array[pos_in_row +
                        2][pos_in_column] == number_to_search) and (array[pos_in_row +
                        3][pos_in_column] == number_to_search):
                    win_value = True
                    return win_value
                else:
                    pos_in_row += 1
            pos_in_row = 0
            pos_in_column += 1
        return win_value

    #Revisado
    def win_right_diagonal(self, array, number_to_search):
        row_size = len(array)
        column_size = len(array[0])
        pos_in_row = 0
        pos_in_column = 0
        win_value = False
        while (pos_in_column + 3) < column_size:
            while (pos_in_row + 3) < row_size:
                if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row +
                        1][pos_in_column + 1] == number_to_search) and (array[pos_in_row +
                        2][pos_in_column + 2] == number_to_search) and (array[pos_in_row +
                        3][pos_in_column + 3] == number_to_search):
                    win_value = True
                    return win_value
                else:
                    pos_in_row += 1
            pos_in_row = 0
            pos_in_column += 1
        return win_value

    #Revisado
    def win_left_diagonal(self, array, number_to_search):
        row_size = len(array)
        column_size = len(array[0])
        pos_in_row = 0
        pos_in_column = 3
        win_value = False
        while (pos_in_row + 3) < row_size:
            while (pos_in_column < column_size):
                if (array[pos_in_row][pos_in_column] == number_to_search) and (array[pos_in_row +
                        1][pos_in_column - 1] == number_to_search) and (array[pos_in_row +
                        2][pos_in_column - 2] == number_to_search) and (array[pos_in_row +
                        3][pos_in_column - 3] == number_to_search):
                       win_value = True
                       return win_value
                else:
                    pos_in_column += 1
            pos_in_column = 3
            pos_in_row += 1
        return win_value

    #Revisado
    def generate_individual_array(self):
        individual_array = []
        count = 0
        while count < 4:
            individual_array.append(random.randint(1, 2))
            count += 1
        return individual_array

    #REVISADO
    def generate_random_population(self):
        random_poblation = []
        count = 0
        while count < 10:
            individual = self.generate_individual_array()
            if individual not in random_poblation:
                random_poblation.append(individual)
                count += 1
        return random_poblation

    def search_array(self, general_array, array_to_search):
        if array_to_search in general_array:
            print("True")
            return True
        else:
            return False

    def random_direction(self):
        direction_array = ["vertical", "horizontal"]
        """,
                           left-diagonal", "right-diagonal"""
        index = random.randint(0, len(direction_array) - 1)
        print(direction_array[index])
        return direction_array[0]

    def random_number(self):
        value = random.randint(1, 2)
        return value

    #REVISADO (ESTA PARTE)
    def generate_population(self, array):
        new_population = []
        if self.matrix_is_empty() == True:
            return self.generate_random_population()
        else:
            count = 0
            while count < 10:
                row_size = len(array)
                column_size = len(array[0])
                pos_in_row = row_size - 1
                pos_in_column = 0
                while count < 10:
                    while pos_in_row > 0:
                        while pos_in_column < column_size:
                            temp_array = []
                            visited_extreme = False
                            if is_extreme(array, i, j):
                                visited_extreme = True
                                if array[pos_in_row][pos_in_column] != 0:
                                    temp_array.append(array[pos_in_row][pos_in_column])
                                    pos_in_row -= 1
                                else:
                                	pos_in_column += 1
                            elif visited_extreme = True and pos_in_row  < row_size - 1:
                            	if array[pos_in_row][pos_in_column] != 0:
                                    temp_array.append(array[pos_in_row][pos_in_column])
                                else:
                                	pos_in_column += 1




















                """
                elif direction == "horizontal":
                    if self.is_extreme(array, pos_in_row, pos_in_column):
                        while pos_in_column <= (column_size - 4):
                            temp_array = []
                            if pos_in_row != row_size - 1:
                                print("ACÁAAAAAAAAAAA ", pos_in_row)
                                if (array[pos_in_row][pos_in_column] != 0) and (array[pos_in_row][pos_in_column 
                                    + 1] != 0) and (array[pos_in_row][pos_in_column +
                                    2] != 0) and (array[pos_in_row][pos_in_column +
                                    3] == 0) and (array[pos_in_row +
                                    1][pos_in_column] != 0) and (array[pos_in_row +
                                    1][pos_in_column +
                                    1] != 0) and (array[pos_in_row +
                                    1][pos_in_column +
                                    2] != 0) and (array[pos_in_row +
                                    1][pos_in_column +
                                    3] != 0):
                                    temp_array.append(
                                        array[pos_in_row][pos_in_column])
                                    temp_array.append(array[pos_in_row][
                                                      pos_in_column + 1])
                                    temp_array.append(array[pos_in_row][
                                                      pos_in_column + 2])
                                    individual = complete_array(temp_array)
                                    new_population.append(individual)
                                    pos_in_column += 1
                                    temp_array = []
                                else:
                                    pos_in_column += 1
                                pos_in_row += 1
                            else:
                                print("ENTRA ACÁ TAMBIEN")
                                if (array[pos_in_row][pos_in_column] != 0) and (array[pos_in_row][pos_in_column + 1] != 0) and (array[pos_in_row][pos_in_column + 2] != 0) and (array[pos_in_row][pos_in_column + 3] == 0):
                                    temp_array.append(
                                        array[pos_in_row][pos_in_column])
                                    temp_array.append(array[pos_in_row][
                                                      pos_in_column + 1])
                                    temp_array.append(array[pos_in_row][
                                                      pos_in_column + 2])
                                    complete_array(temp_array)
                                    pos_in_column += 1
                                    temp_array = []
                                else:
                                    pos_in_column += 1
                            pos_in_row += 1
                        pos_in_row = 0
                        pos_in_column = 0
                    else:
                        print("NO es un extremo")
            count += 1
            """
   	#Revisado
    def complete_array(self, input_array):
        input_array_size = len(input_array)
        while input_array_size < 4:
            input_array.append(self.random_number())
            input_array_size += 1
        print(input_array)
        return input_array

    def execute_generation(self, number_generation=0):
        while number_generation < TOTAL_GENERATIONS:
            population = self.generate_population(self.array)
            self.array = population
            print(population)
        return self.array

array1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
nueva_generacion = Generation(array1, 1)

array2 = nueva_generacion.generate_population(array1)
print(array2)
"""array2 = [1, 2, 1]
nueva_generacion.complete_array(array2)
"""
