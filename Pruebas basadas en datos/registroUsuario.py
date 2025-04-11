import re

# Registrar un usuario si los datos son válidos.
# Comentario prueba Luis
def registrar_usuario(nombre: str, email: str, telefono: str) -> str:
    
    # Validación de nombre no vacío
    if not nombre.strip():
        return "ERROR_NOMBRE"
    
    # Validación básica de email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "ERROR_EMAIL"
    
    # Validación de   teléfono (9 dígitos numéricos)
    if not telefono.isdigit() or len(telefono) != 8:
        return "ERROR_TELEFONO"
    
    return "ÉXITO"
  # Validación básica de email


