from flask import Blueprint, jsonify, request
from flasgger import swag_from


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])

def index():
    return "Olá, este é o endpoint raiz!"

@main.route('/api/hello', methods=['GET'])
@swag_from('../docs/hello.yml')
def hello():
    return jsonify({"message": "Olá, Flask!"})

@main.route('/api/data', methods=['POST'])
def data():
    content = request.json
    return jsonify({"received_data": content})