from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
EXPORTS_PARAM = 'opcao=opt_06' 

exports = Blueprint('exports', __name__)

@exports.route('/api/exports', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, exports!"})

@exports.route('/api/exports/exports', methods=['GET'])
def getProducao():
    return jsonify({"message": "exports"})

