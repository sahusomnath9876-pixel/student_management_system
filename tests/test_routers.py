from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_login():
    data = {
        "username" : "somnath29s",
        "password" : "Sahu@2020"
    }
    response = client.post("auth/signin", json=data)

    assert response.status_code == 200