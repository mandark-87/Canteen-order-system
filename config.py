import os

class Config:
    # MongoDB Configuration - Use environment variables for production
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/canteen_db')
    
    # Application Settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
    
    # Canteen Settings
    OPENING_TIME = "08:00"
    CLOSING_TIME = "22:00"
    TAX_RATE = 0.08  # 8% tax