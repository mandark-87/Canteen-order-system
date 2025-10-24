from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS  # Add this import
from config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Add CORS support - this will fix the cross-origin error
    CORS(app)
    
    # Initialize MongoDB
    mongo.init_app(app)
    
    # Initialize MongoDB with sample data
    with app.app_context():
        from app.models import init_mongodb
        init_mongodb()
    
    # Register blueprints/routes
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app