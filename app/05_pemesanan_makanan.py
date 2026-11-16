from library.function import (
    normalize_text, transform_data, filter_data, aggregate_data,
    calculate_average, sort_data, search_data, flatten_data,
    create_discount, validate_data
)

menu = [
    {"nama": "Nasi Goreng", "kategori": "Makanan", "harga": 18000, "tersedia": True},
    {"nama": "Mie Ayam", "kategori": "Makanan", "harga": 16000, "tersedia": True},
    {"nama": "Es Teh", "kategori": "Minuman", "harga": 5000, "tersedia": False},
    {"nama": "Jus Jeruk", "kategori": "Minuman", "harga": 10000, "tersedia": True},
]

pesanan = [
    {"menu": "Nasi Goreng", "jumlah": 2, "harga": 18000},
    {"menu": "Jus Jeruk", "jumlah": 1, "harga": 10000},
]

@validate_data
def menu_tersedia(data):
    return filter_data(data, lambda item: item["tersedia"])

nama_menu = transform_data(menu, lambda item: normalize_text(item["nama"]))
menu_aktif = menu_tersedia(menu)
hasil_cari = search_data(menu, "mie", "nama")
urut_harga = sort_data(menu, lambda item: item["harga"])
total_bayar = aggregate_data(
    pesanan,
    lambda total, item: total + item["jumlah"] * item["harga"],
    0
)
rata_harga = calculate_average([item["harga"] for item in menu])
diskon_member = create_discount(15)
bayar_member = diskon_member(total_bayar)
opsi_menu = flatten_data([["makanan", ["pedas", "tidak pedas"]], ["minuman"]])

print("=== PEMESANAN MAKANAN ===")
print("Nama menu:", nama_menu)
print("Menu tersedia:", menu_aktif)
print("Pencarian menu:", hasil_cari)
print("Urutan harga:", [item["nama"] for item in urut_harga])
print("Total pembayaran:", total_bayar)
print("Rata-rata harga menu:", rata_harga)
print("Total setelah diskon member:", bayar_member)
print("Opsi menu:", opsi_menu)