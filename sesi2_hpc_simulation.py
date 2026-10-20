import multiprocessing as mp
import time

# Fungsi ini meniru pekerjaan komputasi berulang untuk satu sensor.
# Fungsi simulasi komputasi berat (misal: analisis sensor cuaca lokal)
def hitung_beban_sensor(sensor_id):
    total = sum(i * i for i in range(1000000))
    return f"Sensor {sensor_id} selesai diproses."

# Blok utama mencegah proses berulang saat multiprocessing dijalankan di Windows.
if __name__ == '__main__':
    print("--- SESI 2: Simulasi Komputasi Paralel (HPC) ---")
    start_time = time.time()  # Catat waktu awal.
    
# Pool membuat empat proses pekerja; map membagikan pekerjaan ke proses tersebut.
    with mp.Pool(processes=4) as pool:
        results = pool.map(hitung_beban_sensor, range(4))
        
# Tampilkan status penyelesaian setiap pekerjaan sensor.
    for res in results:
        print(res)
# Tampilkan waktu total sejak komputasi dimulai hingga selesai.
    print(f"Waktu Eksekusi: {time.time() - start_time:.4f} detik")