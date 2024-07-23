from functions.mock import *

def test_api_call_with_mock_1(mock_response):

	"""
	Função para testar o mock de uma chamada de API
	"""

	response = mock_response
	assert response.status_code == 200
	assert response.json() == {"message":"Success"}

def test_api_call_with_mock_2(mock_response):
	response = mock_response
	assert response.status_code == 200
	assert response.json() == {"message":"Success"}

