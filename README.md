# 🍽️ AI Review Analyzer — RM Salero Minang

Sistem otomasi analisis review pelanggan menggunakan 
Claude AI dengan teknik Prompt Chaining 3 tahap.

## 📋 Tentang Proyek
Mengubah 50 review mentah dari Google Maps menjadi 
laporan analisis profesional siap presentasi ke direksi
— secara otomatis dalam hitungan menit.

## ⚙️ Cara Kerja
Input Excel (50 review)
↓
Chain 1 → Klasifikasi sentimen + jenis review
↓
Chain 2 → Agregasi & analisis per kategori
↓
Chain 3 → Laporan eksekutif untuk direksi

## 🛠️ Teknologi
- Python 3.14
- Anthropic Claude API (claude-sonnet-4-6)
- Pandas (baca Excel)
- Teknik: Prompt Chaining, JSON Output Formatting

## 📁 Struktur Folder
Analisis-RM-Salero-Minang/
├── AnalisReview.py               ← program utama
├── config.py                     ← API key (tidak di-upload)
├── data_review_salero_minang.xlsx← data input
├── README.md                     ← dokumentasi ini
└── output/
├── hasil_chain1.json         ← hasil klasifikasi
├── hasil_chain2.json         ← hasil rekap
└── hasil_laporan_direksi.txt ← laporan akhir

## 🚀 Cara Menjalankan
1. Clone repository ini
2. Install dependencies:
   pip install anthropic pandas openpyxl
3. Buat file config.py dan isi API key:
   API_KEY = "sk-ant-xxxx..."
4. Jalankan program:
   python3 AnalisReview.py

## 📊 Contoh Output
- 50 review terklasifikasi otomatis
- Rekap: 26 Positif | 22 Negatif | 2 Netral
- Laporan eksekutif siap presentasi

## 💡 Use Case
Bisa dipakai untuk bisnis apapun yang punya review:
- Restoran & cafe
- Hotel
- Toko online
- Startup

## 👨‍💻 Dibuat dengan
Claude AI + Python