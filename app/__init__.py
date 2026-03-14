import os
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
