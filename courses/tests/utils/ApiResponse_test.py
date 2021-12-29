import unittest

from src.utils.ApiResponse import ApiResponse
from src.app import app


class TestApiResponse(unittest.TestCase):

    def test_ok(self):

        with app.app_context() as context:

            response, status = ApiResponse().set_payload(data={"type": "test-payload"}).OK()
            data = response.get_json()

            assert status == 200
            assert data["type"] == "test-payload"

