from flask import Blueprint, jsonify, request
from flasgger import swag_from

comerce = Blueprint('comerce', __name__)

@comerce.route('/comerce/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, comerce!"})

@comerce.route('/comerce/comerce', methods=['GET'])
def getProducao():
    return jsonify({"message": "comerce"})

