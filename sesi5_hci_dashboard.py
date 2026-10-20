import matplotlib.pyplot as plt

# Data contoh tingkat risiko untuk tiga kategori aset.
# Data hasil analisis untuk ditampilkan ke pengguna
kategori = ['Kategori A', 'Kategori B', 'Kategori C']
nilai = [45, 88, 20]

# Warna merah menonjolkan nilai tertinggi; abu-abu digunakan untuk kategori lain.
# Fitur Visual Preattentive: Memberi warna menonjol pada nilai tertinggi
warna = ['lightgray', 'red', 'lightgray'] 

# Atur ukuran gambar grafik dalam inci.
plt.figure(figsize=(6, 4))
# Membuat diagram batang agar nilai tiap kategori mudah dibandingkan.
plt.bar(kategori, nilai, color=warna)
# Judul dan label sumbu membantu pengguna memahami informasi pada grafik.
plt.title("Dashboard Pengambilan Keputusan (HCI)", fontsize=12)
plt.xlabel("Kategori Aset")
plt.ylabel("Tingkat Risiko")
# Simpan grafik sebagai PNG di folder kerja saat ini.
plt.savefig("dashboard_hci.png")

print("--- SESI 5: Dashboard HCI berhasil disimpan sebagai 'dashboard_hci.png' ---")