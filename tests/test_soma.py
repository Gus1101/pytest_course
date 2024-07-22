from functions.metrics import *

def test_soma():
    """
    Função para testar a soma entre dois valores inteiros
    """
    
    # Arrange
    value1 = 10
    value2 = 20

    # Act
    x = sum_int_values(value1, value2)

    # Assert
    assert x == 30
