from src.services.HealthService import HealthService
from app import app


class TestHealthService:

    def test_get_health(self):

        with app.app_context():

            service_request = HealthService()
            response, status = service_request.get_health()
            data = response.get_json()

            assert status == 200
            assert data == {"status": "UP"}


