from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Data latihan: target 1 berarti pinjaman disetujui, sedangkan 0 berarti ditolak.
# Data histori pelanggan (Fitur: Usia, Pendapatan | Label: 1=Setuju Pinjaman, 0=Tolak)
data = {
    'usia': [25, 45, 35, 50, 23, 40, 60, 20],
    'pendapatan': [3000, 8000, 5000, 9000, 2500, 6000, 10000, 2000],
    'target': [0, 1, 1, 1, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

X = df[['usia', 'pendapatan']]
y = df['target']

# X berisi fitur masukan model; y berisi label yang ingin dipelajari model.

# Data Splitting 80:20 (Sesi 4)
# Pisahkan data: 80% untuk pelatihan dan 20% untuk pengujian. random_state menjaga pembagian tetap.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training Model
# Membuat model Random Forest lalu melatihnya menggunakan data latih.
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluasi
prediksi = model.predict(X_test)

# Akurasi adalah persentase prediksi data uji yang sesuai dengan label sebenarnya.
print("--- SESI 4: Evaluasi Machine Learning ---")
print(f"Akurasi Model: {accuracy_score(y_test, prediksi) * 100}%")