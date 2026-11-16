from customlibrary.library.function import (
    normalize_text, transform_data, filter_data, aggregate_data,
    calculate_average, sort_data, search_data, flatten_data,
    create_discount, validate_data
)

mahasiswa = [
    {"nama": "Alya Putri", "kelas": "A", "nilai": [85, 90, 88]},
    {"nama": "Bima Saputra", "kelas": "B", "nilai": [70, 75, 72]},
    {"nama": "Citra Dewi", "kelas": "A", "nilai": [95, 92, 98]},
]

@validate_data
def mahasiswa_lulus(data):
    return filter_data(
        data,
        lambda item: calculate_average(item["nilai"]) >= 75
    )

nama = transform_data(mahasiswa, lambda item: normalize_text(item["nama"]))
nilai_semua = flatten_data([item["nilai"] for item in mahasiswa])
rata_kelas = calculate_average(nilai_semua)
peringkat = sort_data(
    mahasiswa,
    lambda item: calculate_average(item["nilai"]),
    reverse=True
)
pencarian = search_data(mahasiswa, "citra", "nama")
jumlah_nilai = aggregate_data(nilai_semua, lambda total, nilai: total + nilai, 0)
fungsi_remedial = create_discount(0)  # konfigurasi 0% sebagai contoh closure
hasil_remedial = fungsi_remedial(60)

print("=== AKADEMIK ===")
print("Nama normal:", nama)
print("Mahasiswa lulus:", [item["nama"] for item in mahasiswa_lulus(mahasiswa)])
print("Rata-rata seluruh nilai:", rata_kelas)
print("Peringkat:", [item["nama"] for item in peringkat])
print("Pencarian mahasiswa:", pencarian)
print("Jumlah seluruh nilai:", jumlah_nilai)
print("Contoh nilai setelah konfigurasi:", hasil_remedial)