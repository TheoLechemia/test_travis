from flask import Blueprint, jsonify

api = Blueprint('api', __name__, )


@api.route('/ping')
def ping():
    return jsonify(ping='pong')