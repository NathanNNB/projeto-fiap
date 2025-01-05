from flask import Blueprint, jsonify, request
from flasgger import swag_from

exports = Blueprint('exports', __name__)

@exports.route('/exports/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, exports!"})

@exports.route('/exports/exports', methods=['GET'])
def getProducao():
    return jsonify({"message": "exports"})

