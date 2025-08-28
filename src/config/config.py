import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Config:
    """Konfigurasi dasar aplikasi"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = False

    MODEL_PATH = os.environ.get('MODEL_PATH') or os.path.join(BASE_DIR, 'models', 'gbr_model.joblib')

    API_VERSION = 'v1'
    API_PREFIX = f'/api/{API_VERSION}'

    LOG_LEVEL = os.environ.get('LOG_LEVEL') or 'INFO'
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'