from flask import Blueprint, jsonify, request
from flasgger import swag_from

imports = Blueprint('imports', __name__)

@imports.route('/imports/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, imports!"})

@imports.route('/imports/imports', methods=['GET'])
def getProducao():
    return jsonify({"message": "imports"})

