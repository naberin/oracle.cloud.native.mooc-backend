from flask import jsonify

from src.config.constants import ErrorConstants


class ApiResponse:

    def __init__(self, payload=None):
        self.payload = payload

    def set_payload(self, data):
        self.payload = data
        return self

    def OK(self):
        return jsonify(self.payload), 200

    def CREATED(self):
        return jsonify(self.payload), 201

    def NO_RESPONSE(self):
        return jsonify(), 204

    def NOT_FOUND(self):

        if self.payload:
            return jsonify(self.payload), 404

        else:
            error = ErrorConstants.DEFAULT_NOT_FOUND_ERROR
            detail = ErrorConstants.DEFAULT_NOT_FOUND_DETAIL
            return jsonify(error=error, detail=detail), 404

    def INTERNAL_ERROR(self):
        if self.payload:
            return jsonify(self.payload), 500
        else:
            error = ErrorConstants.DEFAULT_INTERNAL_ERROR
            detail = ErrorConstants.DEFAULT_INTERNAL_DETAIL
            return jsonify(error=error, detail=detail), 500
