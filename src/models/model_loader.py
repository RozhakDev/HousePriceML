import os
import joblib
from pathlib import Path
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)

class ModelLoader:
    """Kelas untuk memuat dan mengelola model machine learning"""

    def __init__(self, model_path: Optional[str] = None):
        """
        Inisialisasi ModelLoader

        Args:
            model_path: Path ke file model. Jika None, akan menggunakan path dari config
        """
        self.model_path = model_path
        self.model = None
        self.is_loaded = False

    def load_model(self) -> Any:
        """
        Memuat model dari file

        Returns:
            Model yang telah dimuat

        Raises:
            FileNotFoundError: Jika file model tidak ditemukan
            Exception: Jika terjadi kesalahan saat memuat model
        """
        try:
            if self.model_path is None:
                from src.config.config import Config
                self.model_path = Config.MODEL_PATH

            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model file not found at: {self.model_path}")

            logger.info(f"Loading model from {self.model_path}")
            self.model = joblib.load(self.model_path)
            self.is_loaded = True

            logger.info("Model loaded successfully")
            return self.model
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise

    def predict(self, data) -> Any:
        """
        Melakukan prediksi menggunakan model yang telah dimuat

        Args:
            data: Data untuk prediksi

        Returns:
            Hasil prediksi

        Raises:
            RuntimeError: Jika model belum dimuat
        """
        if not self.is_loaded or self.model is None:
            raise RuntimeError("Model is not loaded. Call load_model() first.")
        
        try:
            if not isinstance(data, list):
                data = [data]

            prediction = self.model.predict(data)

            return prediction
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise

    def is_model_loaded(self) -> bool:
        """Cek apakah model sudah dimuat"""
        return self.is_loaded and self.model is not None