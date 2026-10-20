# Informatics-Practitioner-Lecture-Series

# Dokumentasi Praktikum Seminar Informatika (Sesi 1–6)

Repositori ini berisi kumpulan program Python yang dikembangkan berdasarkan studi kasus dari enam sesi seminar Informatika. Pembahasan mencakup pengolahan data, pemrosesan paralel, sistem informasi geografis, pembelajaran mesin, interaksi manusia dan komputer, serta pemanfaatan AI untuk mengidentifikasi penyebab deforestasi.

---

### Sesi 1: Make Sense of Data with Analysis and AI

- **Narasumber:** Andria Arisal, S.T., M.Eng. (Pusat Riset Sains Data dan Informasi – BRIN)
- **Studi Kasus:** Analisis Risiko Piutang dan Penentuan Strategi Penanganan Kredit

**Penjelasan dan Implementasi:**

- **Pengolahan Data:** Menyiapkan dataset transaksi simulasi, menghapus data duplikat, mengisi pendapatan yang kosong menggunakan median, dan mengganti piutang kosong dengan nilai 0.
- **Analisis Bisnis:** Menghitung nilai bersih sederhana dari pendapatan dikurangi piutang. Contoh ini berfokus pada tahap awal pengolahan data, belum pada analisis prediktif.
- **Pengembangan Lanjutan:** Data yang telah dibersihkan dapat digunakan untuk mengembangkan model klasifikasi risiko piutang dan simulasi kebijakan kredit.

**File:** `sesi1_data_analytics.py`

---

### Sesi 2: Bridging Global Infrastructure to Address Local Challenges with HPC

- **Narasumber:** Asst. Prof. Dr. Worawan Diaz Carbalo (Thammasat University, Thailand)
- **Studi Kasus:** Simulasi Komputasi Paralel untuk Pemrosesan Data Sensor

**Penjelasan dan Implementasi:**

- **Simulasi Beban Kerja:** Melakukan perhitungan kuadrat bilangan sebagai contoh pekerjaan komputasi berulang untuk beberapa sensor.
- **Pembagian Proses:** Menggunakan modul `multiprocessing` untuk membagikan pekerjaan ke empat proses pekerja.
- **Pengukuran Kinerja:** Mencatat waktu eksekusi total. Perbandingan dengan metode sekuensial dapat ditambahkan untuk mengukur percepatan komputasi.

**File:** `sesi2_hpc_simulation.py`

---

### Sesi 3: Career and Competition in Industrial Era with GIS

- **Narasumber:** Widi Primadepa, S.Kom. (Asset Management GIS Analyst di City Care Property, Selandia Baru)
- **Studi Kasus:** Pemetaan Lokasi Aset Infrastruktur Berdasarkan Informasi Geografis

**Penjelasan dan Implementasi:**

- **Pengelolaan Data Aset:** Menyimpan nama aset serta koordinat lintang dan bujur dalam struktur data Python.
- **Representasi Spasial:** Menggunakan `Point` dari Shapely untuk membentuk geometri lokasi dan `GeoDataFrame` dari GeoPandas untuk menyimpan data spasial.
- **Pengembangan Lanjutan:** Program menampilkan titik lokasi aset. Perhitungan jarak, penentuan prioritas pemeriksaan, dan ekspor GeoJSON dapat ditambahkan kemudian.

**File:** `sesi3_gis_mapping.py`

---

### Sesi 4: Introduction to Machine Learning

- **Narasumber:** Dr. Taniza binti Tajuddin (Universiti Teknologi MARA / UiTM, Malaysia)
- **Studi Kasus:** Klasifikasi Kelayakan Pinjaman Menggunakan Algoritma Random Forest

**Penjelasan dan Implementasi:**

- **Persiapan Dataset:** Membuat data simulasi pemohon pinjaman yang berisi usia, pendapatan, dan label status pinjaman.
- **Pelatihan Model:** Membagi data menjadi data latih dan data uji dengan proporsi 80:20, lalu melatih `RandomForestClassifier`.
- **Pengujian Prediksi:** Mengukur akurasi prediksi pada data uji. Metrik *precision*, *recall*, *F1-score*, dan *confusion matrix* dapat ditambahkan untuk evaluasi lebih lengkap.

**File:** `sesi4_machine_learning.py`

---

### Sesi 5: Human-Computer Interaction & Data Visualization

- **Narasumber:** Dr. Arafat Febriandirza (Kepala Kelompok Riset IMK & Visualisasi – BRIN)
- **Studi Kasus:** Penyajian Informasi Risiko melalui Dashboard Visual

**Penjelasan dan Implementasi:**

- **Penyajian Informasi:** Menampilkan tiga kategori data dalam diagram batang agar nilainya mudah dibandingkan.
- **Penerapan Prinsip Visual:** Menggunakan warna merah untuk menonjolkan nilai tertinggi dan warna abu-abu untuk kategori lainnya.
- **Keluaran Program:** Grafik disimpan sebagai `dashboard_hci.png`. Implementasi saat ini berupa visualisasi statis, belum berupa dashboard interaktif.

**File:** `sesi5_hci_dashboard.py`

---

### Sesi 6: Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

- **Narasumber:** Dr. Bart Slagter (Laboratory of Geo-Information Science & Remote Sensing)
- **Studi Kasus:** Rancangan Awal Model CNN untuk Klasifikasi Citra Satelit

**Penjelasan dan Implementasi:**

- **Arsitektur Model:** Mendefinisikan model *Convolutional Neural Network* (CNN) menggunakan PyTorch dengan lapisan konvolusi dan lapisan linear.
- **Klasifikasi:** Lapisan keluaran menghasilkan dua skor kelas, yaitu deforestasi dan kondisi normal.
- **Batasan Contoh:** Program baru menginisialisasi arsitektur model. Dataset citra, pelatihan, evaluasi, dan identifikasi penyebab deforestasi belum diterapkan.

**File:** `sesi6_satellite_ai.py`

---

## Instalasi dan Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Buka terminal di folder repositori.
3. Pasang pustaka yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan salah satu program, misalnya:

   ```bash
   python sesi1_data_analytics.py
   ```

Setiap file dapat dijalankan secara terpisah. Sesi 5 menghasilkan `dashboard_hci.png` di folder kerja. Sesi 6 membutuhkan instalasi PyTorch yang sesuai dengan sistem operasi dan versi Python.

## Catatan

Seluruh program dalam repositori ini merupakan implementasi pembelajaran menggunakan data simulasi atau contoh sederhana. Hasil perhitungan dan prediksi digunakan untuk memahami konsep serta alur kerja setiap bidang, bukan sebagai pengganti analisis lapangan atau sistem operasional yang telah tervalidasi. Penjelasan README disesuaikan dengan implementasi yang tersedia pada masing-masing file.
