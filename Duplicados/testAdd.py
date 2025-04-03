import add

def test_sumar_positivos():  
    assert add.sumar(2, 3) == 5  
    assert add.sumar(12000, 3) == 12003

def test_sumar_negativos():  
    assert add.sumar(-2, 3) == 1

def test_sumar_cero():  
    assert add.sumar(2, 0) == 2    
    assert add.sumar(0, 0) == 0
    assert add.sumar(0, 2) == 2  

"""
Ejecución:
- Pruebas: 
En la terminal ubicar la carpeta con cd ruta
pytest '.\testAdd.py' -v

- Análisis con sonar
sonar-scanner

https://rules.sonarsource.com/python/
"""