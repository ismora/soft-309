import responses 
import requests  # Para hacer llamadas HTTP
@responses.activate
def test_api_error_handling():
    # Mockear un error 500
    responses.add(
        responses.GET,
        "https://api.example.com/items/999",
        json={"error": "Not found"},
        status=404
    )

    # Ejecutar solicitud y manejar error
    response = requests.get("https://api.example.com/items/999")
    
    assert response.status_code == 404
    assert "error" in response.json()