from functions.bool import *

def test_is_positive():

	"""
	Função para testar se um valor é positivo
	"""

	assert is_positive(5) is True
	assert is_positive(-5) is False
