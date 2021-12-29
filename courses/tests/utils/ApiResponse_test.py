import unittest

from src.utils.ApiResponse import ApiResponse
from src.config.constants import ErrorConstants
from src.app import app


class TestApiResponse(unittest.TestCase):

    def test_set_payload(self):

        test_payload = {"error": "test-error"}
        ar = ApiResponse().set_payload(data=test_payload)

        assert ar.payload == test_payload

    def test_ok(self):

        with app.app_context():

            ar = ApiResponse().set_payload(data={"type": "test-payload"})
            response, status = ar.OK()
            data = response.get_json()

            assert status == 200
            assert data["type"] == "test-payload"

    def test_created(self):

        with app.app_context():

            ar = ApiResponse().set_payload(data={"type": "test-payload"})
            response, status = ar.CREATED()
            data = response.get_json()

            assert status == 201
            assert data["type"] == "test-payload"

    def test_no_response(self):

        with app.app_context():

            ar = ApiResponse().set_payload(data={"type": "test-payload"})
            response, status = ar.NO_RESPONSE()
            data = response.get_json()

            assert status == 204
            assert data == {}

    def test_custom_not_found(self):

        with app.app_context():

            ar = ApiResponse().set_payload(data={"error": "custom-not-found"})
            response, status = ar.NOT_FOUND()
            data = response.get_json()

            assert status == 404
            assert data == {"error": "custom-not-found"}

    def test_default_not_found(self):

        with app.app_context():

            ar = ApiResponse()
            response, status = ar.NOT_FOUND()
            data = response.get_json()

            assert status == 404
            assert data == {
                "error": ErrorConstants.DEFAULT_NOT_FOUND_ERROR,
                "detail": ErrorConstants.DEFAULT_NOT_FOUND_DETAIL
            }

    def test_custom_internal_server_error(self):

        with app.app_context():

            ar = ApiResponse().set_payload({"error": "custom internal server error"})
            response, status = ar.INTERNAL_ERROR()
            data = response.get_json()

            assert status == 500
            assert data == {"error": "custom internal server error"}

    def test_default_internal_server_error(self):

        with app.app_context():

            ar = ApiResponse()
            response, status = ar.INTERNAL_ERROR()
            data = response.get_json()

            assert status == 500
            assert data == {
                "error": ErrorConstants.DEFAULT_INTERNAL_ERROR,
                "detail": ErrorConstants.DEFAULT_INTERNAL_DETAIL
            }
