import torch
import torch.nn as nn

# Contoh arsitektur CNN sederhana; model ini belum dilatih dengan citra sungguhan.
# Simulasi arsitektur CNN sederhana untuk klasifikasi citra satelit
class SatelliteCNN(nn.Module):
    def __init__(self):
        super(SatelliteCNN, self).__init__()
        # Inisialisasi bagian dari kelas induk PyTorch.
        # Lapisan konvolusi menerima 3 kanal warna RGB dan menghasilkan 16 feature maps.
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3) # Input 3 channel (RGB citra)
        # Lapisan linear menghasilkan skor untuk dua kelas: deforestasi dan normal.
        self.fc = nn.Linear(16 * 62 * 62, 2) # Output 2 kelas (Deforestasi / Normal)

    def forward(self, x):
        # Terapkan konvolusi lalu fungsi aktivasi ReLU.
        x = torch.relu(self.conv1(x))
        # Ratakan feature maps menjadi vektor agar bisa diproses lapisan linear.
        x = x.view(x.size(0), -1)
        # Kembalikan skor untuk dua kelas; skor ini belum berupa probabilitas.
        return self.fc(x)

# Membuat model dengan bobot awal. Belum ada proses pelatihan atau prediksi citra.
model = SatelliteCNN()
print("--- SESI 6: Model AI Citra Satelit Berhasil Diinisialisasi ---")
print(model)