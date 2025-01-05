from flask import Blueprint, jsonify, request
from flasgger import swag_from

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])

def index():
    return "Olá, este é o endpoint raiz!"

@main.route('/api/hello', methods=['GET'])
@swag_from({
    'tags': ['Hello'],
    'description': 'Endpoint que retorna uma saudação.',
    'responses': {
        200: {
            'description': 'Sucesso',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Hello, Flask!'
                    }
                }
            }
        }
    }
})
def hello():
    return jsonify({"message": "Olá, Flask!"})

@main.route('/api/processing', methods=['GET'])
def getProducao():
    query = request.args.get('year', default='', type=int)
    return jsonify({"message": query})

