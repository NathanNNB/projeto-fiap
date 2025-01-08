import os
from flask import Flask, request, redirect
from app.routes import create_app
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Porta definida pela Render
    app.run(host="0.0.0.0", port=port)