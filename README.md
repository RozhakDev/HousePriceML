# HousePriceML - Prediksi Harga Rumah

**HousePriceML** adalah aplikasi berbasis Flask yang digunakan untuk deployment dan monitoring model machine learning. Proyek ini berfokus pada kasus prediksi harga rumah dengan model regresi yang dapat memberikan hasil prediksi secara real-time melalui API.

## ✨ Fitur

* **Health Check:** Memastikan status aplikasi berjalan dengan baik dan model berhasil dimuat.
* **Prediksi:** Memberikan hasil prediksi harga rumah berdasarkan data input.

## 🛠️ Instalasi dan Penggunaan

1. **Clone Repositori**
   Clone repositori ini ke perangkat lokalmu:
   
   ```bash
   git clone https://github.com/RozhakDev/HousePriceML.git
   cd HousePriceML
   ```

2. **Install Dependensi**
   Pastikan kamu sudah menginstal Python 3.6+. Lalu, instal semua dependensi:
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Letakkan Model**
    Pastikan file model (`gbr_model.joblib`) berada di folder `models/`.

4. **Jalankan Aplikasi**
   Jalankan server Flask:
   
   ```bash
   python run.py
   ```

Aplikasi akan berjalan di `http://127.0.0.1:5000`.

## 📡 API Endpoints

### 1. Prediksi

* **Endpoint:** `POST /predict`

* **Deskripsi:** Mengirim data input untuk mendapatkan hasil prediksi.

* **Request Body:**
  
  ```json
  {
  "data": [[value1, value2, ...]]
  }
  ```

* **Response:**
  
  ```json
    {
    "success": true,
    "prediction": [result1, result2, ...]
    }
  ```

### 2. Health Check

* **Endpoint:** `GET /api/v1/health`

* **Deskripsi:** Mengecek status kesehatan aplikasi dan memastikan model telah berhasil dimuat.

* **Response:**
  
  ```json
  {
    "status": "healthy",
    "model_loaded": true
    }
  ```

## 📌 Catatan Penting

1. **Pentingnya Versi Library:** Gunakan versi yang sama untuk Python, `joblib`, dan `scikit-learn` seperti yang digunakan saat melatih dan menyimpan model. Ini bertujuan untuk mencegah konflik dependencies.
2. **Persyaratan Input:** Pastikan data input dikirim dalam format JSON dengan daftar nilai yang diperlukan untuk prediksi.

## ❤️ Penutup

HousePriceML dirancang untuk membantu pengguna akhir memanfaatkan prediksi harga rumah dengan mudah. Kami berharap aplikasi ini dapat menjadi inspirasi dan bermanfaat bagi banyak orang. Jika ada pertanyaan atau saran, silakan hubungi kami melalui GitHub.