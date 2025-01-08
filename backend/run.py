import os
from flask import Flask, request, redirect
from app.routes import create_app
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "https://projeto-fiap-coral.vercel.app"}})

@app.before_request
def enforce_https_in_production():
    if os.getenv("FLASK_ENV") == "production" and not request.is_secure:
        url = request.url.replace("http://", "https://", 1)
        app.logger.info(f"Requisição recebida: {request.url}")
        app.logger.info(f"Requisição final: {request.url}")
        app.logger.info(f"getEnv FLASK ENV: {os.getenv("FLASK_ENV")}")
        app.logger.info(f"request.is_secure: {request.is_secure}")
        return redirect(url, code=301)

@app.route("/api/processing")
def processing():
    return {"message": "Requisição processada com sucesso!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
