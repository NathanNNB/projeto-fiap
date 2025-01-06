from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
IMPORTS_PARAM = 'opcao=opt_05' 

imports = Blueprint('imports', __name__)

@imports.route('/api/imports/imports', methods=['GET'])
def getImports():
    return jsonify({"message": "imports"})

