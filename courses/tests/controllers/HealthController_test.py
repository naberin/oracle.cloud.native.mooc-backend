import json

from app import app


class TestHealthController:

    def test_get_health(self):
        with app.test_client() as client:
            response = client.get("/api/health")
            data = json.loads(response.data)

            assert data["status"] == "UP"


