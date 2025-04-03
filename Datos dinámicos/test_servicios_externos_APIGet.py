import responses 
import requests  # Para hacer llamadas HTTP

@responses.activate  # Habilita el mock para esta prueba
def test_get_user():
    # Configurar el mock
    user_id = "user_123"
    mock_response = {
        "id": user_id,
        "name": "John Doe",
        "email": "john@example.com"
    }

    # 1. Definir qué URL y respuesta mockear
    responses.add(
        responses.GET,  # Método HTTP a mockear
        f"https://api.example.com/users/{user_id}",  # URL esperada
        json=mock_response,  # Respuesta simulada
        status=200  # Código HTTP simulado
    )

    # 2. Ejecutar la solicitud HTTP (simulada)
    response = requests.get(f"https://api.example.com/users/{user_id}")

    # 3. Verificar la respuesta
    assert response.status_code == 200
    assert response.json()["id"] == user_id
    assert len(responses.calls) == 1  # ¿Se llamó a la API una vez?