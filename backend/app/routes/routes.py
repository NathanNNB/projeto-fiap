from flask import Blueprint, jsonify
from flasgger import swag_from
from app.services.scraping_service import scrape_page
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("BASE_URL")

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
