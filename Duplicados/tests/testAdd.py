import pytest
from add import sumar

def test_sumar_positivos():
    """Test suma de números positivos"""
    assert sumar(2, 3) == 5
    assert sumar(12000, 3) == 12003

def test_sumar_negativos():
    """Test suma con números negativos"""
    assert sumar(-2, 3) == 1
    assert sumar(-5, -3) == -8  # Caso adicional para coverage

def test_sumar_cero():
    """Test casos con cero"""
    assert sumar(2, 0) == 2
    assert sumar(0, 0) == 0
    assert sumar(0, 2) == 2

def test_sumar_decimales():
    """Test suma con decimales"""
    assert sumar(2.5, 3.1) == pytest.approx(5.6)  

"""
Ejecución: Desntro de la carpeta test
pytest .\testAdd.py -v --cov=add --cov-report=xml

python -m coverage xml
python -m codacy_coverage

"""