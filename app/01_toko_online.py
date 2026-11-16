from customlibrary.library.function import (
    normalize_text, transform_data, filter_data, aggregate_data,
    calculate_average, sort_data, search_data, flatten_data,
    create_discount, validate_data
)

produk = [
    {"nama": "Laptop", "kategori": "Elektronik", "harga": 12000000, "stok": 5},
    {"nama": "Mouse", "kategori": "Aksesoris", "harga": 150000, "stok": 20},
    {"nama": "Keyboard", "kategori": "Aksesoris", "harga": 350000, "stok": 0},
    {"nama": "Monitor", "kategori": "Elektronik", "harga": 2500000, "stok": 8},
]

# Fungsi library dipakai sebagai komponen pengolahan katalog dan transaksi.
@validate_data
def katalog_tersedia(data):
    return filter_data(data, lambda item: item["stok"] > 0)

nama_produk = transform_data(produk, lambda item: normalize_text(item["nama"]))
produk_tersedia = katalog_tersedia(produk)
hasil_cari = search_data(produk, "key", "nama")
produk_termurah = sort_data(produk, lambda item: item["harga"])
harga_diskon = create_discount(10)(produk[0]["harga"])
total_stok = aggregate_data(produk, lambda total, item: total + item["stok"], 0)
rata_rata_harga = calculate_average([item["harga"] for item in produk])
data_varian = flatten_data([["reguler", ["premium"]], ["hemat"]])

print("=== TOKO ONLINE ===")
print("Nama produk normal:", nama_produk)
print("Produk tersedia:", katalog_tersedia(produk_tersedia))
print("Hasil pencarian:", hasil_cari)
print("Urutan harga:", [item["nama"] for item in produk_termurah])
print("Harga Laptop setelah diskon 10%:", harga_diskon)
print("Total stok:", total_stok)
print("Rata-rata harga:", rata_rata_harga)
print("Varian:", data_varian)
