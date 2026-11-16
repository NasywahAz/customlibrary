from customlibrary.library.function import (
    normalize_text, transform_data, filter_data, aggregate_data,
    calculate_average, sort_data, search_data, flatten_data,
    create_discount, validate_data
)

buku = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2022, "tersedia": True},
    {"judul": "Pemrograman Fungsional", "penulis": "Budi", "tahun": 2024, "tersedia": True},
    {"judul": "Struktur Data", "penulis": "Citra", "tahun": 2021, "tersedia": False},
]

@validate_data
def buku_tersedia(data):
    return filter_data(data, lambda item: item["tersedia"])

judul_normal = transform_data(buku, lambda item: normalize_text(item["judul"]))
hasil_cari = search_data(buku, "python", "judul")
urut_tahun = sort_data(buku, lambda item: item["tahun"], reverse=True)
jumlah_buku = aggregate_data(buku, lambda total, item: total + 1, 0)
rata_tahun = calculate_average([item["tahun"] for item in buku])
denda_harian = create_discount(0)(5000)  # contoh konfigurasi tarif tanpa diskon
kategori = flatten_data([["teknologi", ["pemrograman"]], ["referensi"]])

print("=== PERPUSTAKAAN ===")
print("Judul:", judul_normal)
print("Buku tersedia:", buku_tersedia(buku))
print("Pencarian:", hasil_cari)
print("Urutan tahun terbaru:", [item["judul"] for item in urut_tahun])
print("Jumlah buku:", jumlah_buku)
print("Rata-rata tahun terbit:", rata_tahun)
print("Contoh tarif denda:", denda_harian)
print("Kategori:", kategori)