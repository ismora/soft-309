from faker import Faker
import responses
import requests

fake = Faker()

def test_external_api():
    with responses.RequestsMock() as mock:
        expected_data = {"id": fake.uuid4(), "status": "success"}
        mock.add(
            responses.GET,
            "https://api.example.com/data",
            json=expected_data,
            status=200,
        )
        response = requests.get("https://api.example.com/data")
        assert response.json()["id"] == expected_data["id"]