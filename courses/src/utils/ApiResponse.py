from flask import jsonify


class ApiResponse:

    def __init__(self, payload=None):
        self.payload = payload

    def set_payload(self, data):
        self.payload = data
        return self

    def OK(self):
        return jsonify(self.payload), 200
