from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .routes import main
from .scraping.production import production
from .scraping.processing import processing
from .scraping.comerce import comerce
from .scraping.imports import imports
from .scraping.exports import exports

def create_app():
    app = Flask(__name__)
    CORS(app)  # <--- aqui, liberando o CORS por padrão
    
    app.config['SWAGGER'] = {
        'title': 'Minha API Flask',
        'uiversion': 3,
        'auth_config': {},
    }

    swagger = Swagger(app)
    
    app.register_blueprint(main)
    app.register_blueprint(production)
    app.register_blueprint(processing)
    app.register_blueprint(comerce)
    app.register_blueprint(imports)
    app.register_blueprint(exports)
    return app