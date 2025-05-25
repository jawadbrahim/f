import os
from dataclasses import dataclass
@dataclass
class Development:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT =os.getenv("REDIS_PORT")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    JWT_SECRET=os.getenv("JWT_SECRET")
    KEY=os.getenv("KEY")
    FIREBASE_PATH= os.getenv("FIREBASE_PATH")
    # DB_HOST = os.getenv('DB_HOST')
    # DB_USER = os.getenv('DB_USER')
    # DB_PASS = os.getenv('DB_PASS')
    # DB_NAME = os.getenv('DB_NAME')
 
    
