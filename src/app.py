from flask import Flask
import logging
import os
from pathlib import Path

from src.api.endpoints import api_bp, initialize_model
from src.config.config import Config

def create_app(config_object: object = Config) -> Flask:
    """
    Fungsi pabrik untuk membuat instance Flask

    Args:
        config_object: Objek konfigurasi yang akan digunakan

    Returns:
        Instance Flask yang dikonfigurasi
    """
    app = Flask(__name__)

    app.config.from_object(config_object)

    setup_logging(app)

    app.register_blueprint(api_bp)

    with app.app_context():
        model_initialized = initialize_model()
        if not model_initialized:
            logging.warning("Failed to initialize model. API may not work properly.")

    @app.route('/')
    def index():
        """Halaman root dengan informasi tentang API"""
        return {
            'message': 'Machine Learning Model API',
            'version': '1.0.0',
            'endpoints': {
                'predict': '/api/v1/predict',
                'health': '/api/v1/health'
            }
        }
    
    @app.errorhandler(404)
    def not_found(error):
        return {
            'error': 'Not Found',
            'message': 'The requested resource was not found'
        }, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred'
        }, 500
    
    return app

def setup_logging(app: Flask) -> None:
    """
    Setup logging untuk aplikasi

    Args:
        app: Instance Flask
    """
    log_level = getattr(logging, app.config['LOG_LEVEL'].upper(), logging.INFO)
    log_format = app.config['LOG_FORMAT']

    formatter = logging.Formatter(log_format)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    log_file = os.path.join(app.config.get('BASE_DIR', '.'), 'app.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    app.logger.addHandler(console_handler)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)

    logging.getLogger('werkzeug').setLevel(log_level)

def run_app(debug=False, host='0.0.0.0', port=5000):
    """
    Fungsi untuk menjalankan aplikasi Flask

    Args:
        debug: Mode debugging
        host: Host untuk menjalankan aplikasi
        port: Port untuk menjalankan aplikasi
    """
    app = create_app()

    app.run(host=host, port=port, debug=debug)

app = create_app()