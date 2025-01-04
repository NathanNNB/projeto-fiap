from flask import Flask
from flask_cors import CORS
from .routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)  # <--- aqui, liberando o CORS por padrão
    app.register_blueprint(main)
    return app