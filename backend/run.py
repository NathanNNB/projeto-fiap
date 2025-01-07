import os
from flask import Flask, request, redirect
from app.routes import create_app

app = create_app()

@app.before_request
def enforce_https_in_production():
    # Verifica se está em produção
    if os.getenv("FLASK_ENV") == "production" and request.url.startswith("http://"):
        url = request.url.replace("http://", "https://", 1)
        return redirect(url, code=301)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)