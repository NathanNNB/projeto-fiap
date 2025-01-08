import os
from flask import Flask, request, redirect
from app.routes import create_app
from flask_cors import CORS

app = create_app()

CORS(app, resources={r"/api/*": {"origins": "https://projeto-fiap-coral.vercel.app"}})

@app.before_request
def enforce_https_in_production():
    if os.getenv("FLASK_ENV") == "production":
        url = request.url.replace("http://", "https://", 1)
        app.logger.info(f"Redirecionando: {request.url} -> {url}")
        return redirect(url, code=301)

if __name__ == "__main__":
    print(os.getenv("FLASK_ENV"))
    debug_mode = os.getenv("FLASK_ENV") != "production"
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=debug_mode)