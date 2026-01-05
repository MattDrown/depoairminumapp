# 📍 Sistem Informasi Geografis - Depo Asyifa

Aplikasi berbasis web untuk manajemen data pelanggan dan distribusi logistik Depo Asyifa. Aplikasi ini dirancang untuk mempermudah operasional internal dalam mendata titik lokasi pelanggan secara akurat menggunakan koordinat GPS dan bukti foto.

## 🚀 Fitur Utama

### 🗺️ Dashboard Pemetaan
- **Peta Interaktif:** Visualisasi sebaran pelanggan secara *full-screen* menggunakan OpenStreetMap & Leaflet.js.
- **Smart Search:** Pencarian pelanggan berdasarkan nama dengan fitur *Auto-Zoom* (FlyTo) ke titik lokasi.
- **Detail Popup:** Menampilkan info detail (Nama, Alamat, Foto Depo/Rumah) saat pin diklik.

### 📱 Input Data Lapangan (Kurir Mode)
- **Real-time GPS Tracking:** Mengambil koordinat (Latitude/Longitude) kurir secara otomatis dengan akurasi tinggi.
- **Mobile Friendly:** Antarmuka khusus untuk input data via HP.
- **Upload Foto:** Fitur upload foto lokasi/rumah pelanggan langsung dari kamera HP.

### 🛠️ Panel Admin
- **Map Picker:** Input koordinat pelanggan di Admin Panel tinggal klik titik di peta (tidak perlu ketik manual).
- **Manajemen Data:** CRUD (Create, Read, Update, Delete) data pelanggan terpusat.

## 💻 Teknologi yang Digunakan

- **Backend:** Python Django 5.x
- **Database:** SQLite (Development)
- **Frontend:** HTML5, CSS3, JavaScript
- **Maps API:** Leaflet.js + OpenStreetMap (Free & Open Source)
- **Styling:** CSS Native (Custom Responsive Design)

## 📸 Screenshots

*(Nanti kamu bisa upload screenshot peta atau form input di sini biar makin keren)*

## 📦 Cara Instalasi (Local)

1. **Clone Repository**
   ```bash
   git clone [https://github.com/username-kamu/depo-asyifa.git](https://github.com/username-kamu/depo-asyifa.git)
   cd depo-asyifa
