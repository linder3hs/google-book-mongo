from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import Config
from app.routes.book import book_router

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    Bootstrap(app)

    app.register_blueprint(book_router)

    return app
