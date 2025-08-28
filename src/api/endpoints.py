from flask import Blueprint, request, jsonify
import logging
from typing import Dict, Any, Optional

from src.models.model_loader import ModelLoader

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

model_loader = ModelLoader()

def initialize_model():
    """Fungsi untuk menginisialisasi model saat aplikasi dimulai"""
    try:
        model_loader.load_model()
        return True
    except Exception as e:
        logging.error(f"Failed to initialize model: {str(e)}")
        return False

@api_bp.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint untuk melakukan prediksi

    Expected JSON format:
    {
        "data": [nilai1, nilai2, ...]
    }

    Returns:
        JSON dengan hasil prediksi
    """
    try:
        if not model_loader.is_model_loaded():
            return jsonify({
                'error': 'Model is not loaded',
                'message': 'Please try again later'
            }), 500
        
        json_data = request.get_json()

        if not json_data or 'data' not in json_data:
            return jsonify({
                'error': 'Invalid input',
                'message': 'Please provide data in the format: {"data": [value1, value2, ...]}'
            }), 400
        
        data = json_data['data']

        if not isinstance(data, list):
            return jsonify({
                'error': 'Invalid data type',
                'message': 'Data should be a list of values'
            }), 400

        prediction = model_loader.predict(data)

        return jsonify({
            'success': True,
            'prediction': prediction.tolist()
        }), 200
    except Exception as e:
        logging.error(f"Error in prediction endpoint: {str(e)}")
        return jsonify({
            'error': 'Prediction failed',
            'message': 'An internal error occurred'
        }), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint untuk cek kesehatan aplikasi

    Returns:
        JSON dengan status kesehatan aplikasi
    """
    try:
        model_loaded = model_loader.is_model_loaded()

        return jsonify({
            'status': 'healthy',
            'model_loaded': model_loaded
        }), 200
    except Exception as e:
        logging.error(f"Error in health check endpoint: {str(e)}")
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500