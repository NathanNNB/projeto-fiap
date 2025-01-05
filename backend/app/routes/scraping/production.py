from flask import Blueprint, jsonify, request
from flasgger import swag_from

production = Blueprint('production', __name__)

@production.route('/production/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, Production!"})

@production.route('/production/production', methods=['GET'])
def getProducao():
    return jsonify({"message": "Production"})

