from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .routes import main

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
    return app