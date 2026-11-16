from library.function import (
    normalize_text, transform_data, filter_data, aggregate_data,
    calculate_average, sort_data, search_data, flatten_data,
    create_discount, validate_data
)

barang = [
    {"nama": "Kertas A4", "lokasi": "Gudang A", "stok": 12, "harga": 55000},
    {"nama": "Tinta Printer", "lokasi": "Gudang B", "stok": 3, "harga": 85000},
    {"nama": "Pulpen", "lokasi": "Gudang A", "stok": 50, "harga": 3000},
]

@validate_data
def stok_menipis(data):
    return filter_data(data, lambda item: item["stok"] < 10)

nama_barang = transform_data(barang, lambda item: normalize_text(item["nama"]))
peringatan = stok_menipis(barang)
urut_stok = sort_data(barang, lambda item: item["stok"])
cari_tinta = search_data(barang, "tinta", "nama")
total_unit = aggregate_data(barang, lambda total, item: total + item["stok"], 0)
rata_harga = calculate_average([item["harga"] for item in barang])
diskon_supplier = create_discount(5)
harga_kertas = diskon_supplier(barang[0]["harga"])
lokasi = flatten_data([["Gudang A", ["Rak 1", "Rak 2"]], ["Gudang B"]])

print("=== INVENTARIS ===")
print("Nama barang:", nama_barang)
print("Peringatan stok:", peringatan)
print("Urutan stok:", [item["nama"] for item in urut_stok])
print("Pencarian tinta:", cari_tinta)
print("Total unit:", total_unit)
print("Rata-rata harga:", rata_harga)
print("Harga kertas setelah diskon supplier:", harga_kertas)
print("Lokasi penyimpanan:", lokasi)