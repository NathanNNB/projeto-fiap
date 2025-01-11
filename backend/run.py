import os
from flask import Flask, request, redirect
from app.routes import create_app
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.before_request
def enforce_https_in_production():
    if os.getenv("FLASK_ENV") == "production":
        # Verifica se o cabeçalho enviado pelo Render indica HTTPS
        if request.headers.get("X-Forwarded-Proto", "http") != "https":
            url = request.url.replace("http://", "https://", 1)
            return redirect(url, code=301)
        
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Porta definida pela Render
    app.run(host="0.0.0.0", port=port)