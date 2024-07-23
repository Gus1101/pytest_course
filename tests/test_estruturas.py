def test_equal_lists():

	"""
	Função para testar se as listas são iguais. Retorna uma mensagem caso as listas não sejam iguais
	"""

	expected_list = [1,2,3,4,5]
	results_list = [1,2,3,4,5]
	assert expected_list == results_list, "As listas não são iguais"
