def test_soma():
    """
    Função para testar a soma entre dois valores inteiros
    """
    
    # Arrange
    valor1 = 10
    valor2 = 20

    # Act
    x = sum([valor1,valor2])

    # Assert
    assert x == 30