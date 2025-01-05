from flask import Blueprint, jsonify, request
from flasgger import swag_from

processing = Blueprint('processing', __name__)

@processing.route('/processing/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, processing!"})

@processing.route('/processing/processing', methods=['GET'])
def getProducao():
    return jsonify({"message": "processing"})

