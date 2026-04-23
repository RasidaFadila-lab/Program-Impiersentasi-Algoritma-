# Struktur Data: List yang berisi Dictionary
# Nilai disimpan dalam Tuple di dalam Dictionary
data_mahasiswa = [
    {"nama": "Budi Santoso", "nim": "2021001", "nilai": (80, 85, 90)},
    {"nama": "Siti Aminah", "nim": "2021002", "nilai": (95, 90, 92)},
    {"nama": "Iwan Fals", "nim": "2021003", "nilai": (70, 75, 80)},
    {"nama": "Dewi Sartika", "nim": "2021004", "nilai": (88, 82, 85)}
]

# --- TUGAS 01: Menampilkan seluruh data mahasiswa ---
print("=== DATA MAHASISWA ===")
for mhs in data_mahasiswa:
    print(f"Nama: {mhs['nama']} | NIM: {mhs['nim']} | Nilai: {mhs['nilai']}")

print("-" * 30)

# --- TUGAS 02: Menghitung rata-rata nilai tiap mahasiswa ---
print("=== RATA-RATA NILAI ===")
rekap_rata_rata = [] # Untuk menyimpan hasil rata-rata

for mhs in data_mahasiswa:
    # Mengambil tuple nilai
    nilai = mhs['nilai']
    # Menghitung rata-rata: jumlah total / banyak mata kuliah
    rata_rata = sum(nilai) / len(nilai)
    
    # Menampilkan hasil
    print(f"Mahasiswa: {mhs['nama']} | Rata-rata: {rata_rata:.2f}")
    
    # Menyimpan data untuk Tugas 03
    rekap_rata_rata.append({
        "nama": mhs['nama'],
        "rata_rata": rata_rata
    })

print("-" * 30)

# --- TUGAS 03: Menentukan mahasiswa dengan nilai rata-rata tertinggi ---
print("=== MAHASISWA TERBAIK ===")
# Menggunakan fungsi max dengan key rata_rata
terbaik = max(rekap_rata_rata, key=lambda x: x['rata_rata'])

print(f"Mahasiswa dengan rata-rata tertinggi adalah {terbaik['nama']} ")
print(f"dengan nilai: {terbaik['rata_rata']:.2f}")
