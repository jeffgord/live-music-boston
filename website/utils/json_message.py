from flask import jsonify


def success_message(message="All good"):
    return jsonify({"status": "success", "message": message})


def error_message(exception=None):
    message = str(exception) if exception else "Something went wrong"
    return jsonify({"status": "error", "message": message})
