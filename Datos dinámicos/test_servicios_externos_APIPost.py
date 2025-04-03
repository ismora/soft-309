import responses 
import requests  # Para hacer llamadas HTTP

@responses.activate
def test_create_user():
    # Configurar el mock
    mock_response = {"id": "user_456", "status": "created"}
    request_data = {"name": "Alice", "email": "alice@example.com"}

    # Mockear POST a /users
    responses.add(
        responses.POST,
        "https://api.example.com/users",
        json=mock_response,
        status=201
    )

    # Ejecutar la solicitud POST
    response = requests.post(
        "https://api.example.com/users",
        json=request_data
    )

    # Verificar respuesta y datos enviados
    assert response.status_code == 201
    assert response.json()["status"] == "created"
    
    # Validar que los datos enviados son correctos
    request_sent = responses.calls[0].request
    assert request_sent.method == "POST"
    assert request_sent.headers["Content-Type"] == "application/json"
    assert request_sent.body == b'{"name": "Alice", "email": "alice@example.com"}'