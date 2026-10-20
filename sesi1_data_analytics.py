import pandas as pd

# Dataset simulasi transaksi; None berarti nilainya belum tersedia.
# Data mentah transaksi bisnis
raw_data = {
    'transaksi_id': [101, 102, 103, 103, 104, 105],
    'pendapatan': [5000, 7000, None, 6000, 8000, None],
    'piutang': [1000, 2000, 1500, 1500, None, 3000]
}

df = pd.DataFrame(raw_data)

# Mengubah dictionary menjadi DataFrame agar mudah diolah dengan pandas.

# 1. Hapus duplikat
# Menghapus baris yang duplikat secara keseluruhan.
df = df.drop_duplicates()

# 2. Isi nilai NaN dengan menampungnya kembali ke kolom
# Mengisi pendapatan kosong dengan median, sedangkan piutang kosong dianggap 0.
df['pendapatan'] = df['pendapatan'].fillna(df['pendapatan'].median())
df['piutang'] = df['piutang'].fillna(0)

# 3. Hitung total bersih
# Menghitung nilai bersih sederhana setelah piutang dikurangi dari pendapatan.
df['total_bersih'] = df['pendapatan'] - df['piutang']

print("--- SESI 1: Data Transaksi Bersih ---")
print(df)