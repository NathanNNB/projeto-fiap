from flask import Blueprint, jsonify, request
from flasgger import swag_from

URL_1 = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
url_2 = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano=1970&opcao=opt_02"

production = Blueprint('production', __name__)

@production.route('/api/production', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, Production!"})

@production.route('/api/production/production', methods=['GET'])
def getProducao():
    return jsonify({"message": "Production"})

