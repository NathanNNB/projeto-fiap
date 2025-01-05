from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
IMPORTS_PARAM = 'opcao=opt_05' 

imports = Blueprint('imports', __name__)

@imports.route('/api/imports', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, imports!"})

@imports.route('/api/imports/imports', methods=['GET'])
def getProducao():
    return jsonify({"message": "imports"})

