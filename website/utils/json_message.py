from flask import jsonify
from http import HTTPStatus


def success(message="All good"):
    return jsonify({"status": "success", "message": message}), HTTPStatus.OK


def error(message="Something went wrong unexpectedly"):
    return (
        jsonify({"status": "error", "message": message}),
        HTTPStatus.INTERNAL_SERVER_ERROR,
    )
