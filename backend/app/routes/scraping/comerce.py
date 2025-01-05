from flask import Blueprint, jsonify, request
from flasgger import swag_from

comerce = Blueprint('comerce', __name__)

@comerce.route('/api/comerce', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, comerce!"})

@comerce.route('/api/comerce/comerce', methods=['GET'])
def getProducao():
    return jsonify({"message": "comerce"})

