import os

class Config:
    #UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    # Add other configuration variables as needed

config = Config()
