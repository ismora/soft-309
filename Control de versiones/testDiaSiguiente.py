from source_code import dia_siguiente

def testDiaSiguiente():
    assert dia_siguiente((2025, 2, 28)) == (2025, 3, 1)

"""
Ejecución en la terminal (dentro de la carpeta Control de versiones): pytest .\testDiaSiguiente.py -v
"""