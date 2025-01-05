from flask import Blueprint, jsonify, request
from flasgger import swag_from

processing = Blueprint('processing', __name__)

@processing.route('/api/processing', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, processing!"})

@processing.route('/api/processing/processing', methods=['GET'])
def getProducao():
    return jsonify({"message": "processing"})

