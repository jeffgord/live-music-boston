from flask import jsonify


def success(message="All good"):
    return jsonify({"status": "success", "message": message})


def error(message="Something went wrong unexpectedly"):
    return jsonify({"status": "error", "message": message})
