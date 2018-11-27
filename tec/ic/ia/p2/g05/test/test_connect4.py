from g05.connect4 import GeneticConnect4
import pytest 

new_connect4 = None

@pytest.fixture
def setup_class():
	global new_connect4
	new_connect4 = GeneticConnect4()

def test_set_player(setup_class):
	value = new_connect4.set_player("HUMANO", "MÁQUINA")
	assert value == 0

"""
def test_main_menu(setup_class):
    input_value = 1
    output = []

    def mock_input(s):
        output.append(s)
        return input_values
    new_connect4.input = mock_input
    new_connect4.print = lambda s : output.append(s)
    new_connect4.main_menu() 
    assert output == [
        'First: ',
        'Second: ', 
        'The result is 5',
    ]
"""