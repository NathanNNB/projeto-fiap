from flask import Blueprint, jsonify
from flasgger import swag_from
from app.services.scraping_service import scrape_page

URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

main = Blueprint('main', __name__)


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
def getProcessing():
    url = URL
    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    try:
        h2_list = scrape_page(url)
        return jsonify({'h2_tags': h2_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

