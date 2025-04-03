import registroUsuario
import pytest
import csv

print("Pruebas del registro de usuario")
def leer_datos_registro():
    with open('datos_prueba.csv', encoding="utf-8") as file:
        return list(csv.reader(file))


@pytest.mark.parametrize("nombre,email,telefono,resultado_esperado", leer_datos_registro())
def test_registro_usuario(nombre, email, telefono, resultado_esperado):
    resultado_real = registroUsuario.registrar_usuario(nombre, email, telefono)
    assert resultado_real == resultado_esperado, f"Falló con: {nombre}, {email}, {telefono}"

"""
Cobertura completa: Se prueban combinaciones de: 
1.Campos vacíos 
2.Formatos inválidos 
3.Datos con espacios 
4.Casos válidos e inválidos mezclados

Para agregar un nuevo tipo de error (por ejemplo: validar longitud del nombre). Solo se modifica la función registrar_usuario y no los tests
"""

