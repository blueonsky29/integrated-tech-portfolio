"""
generate_data.py
Membuat dataset penjualan UMKM yang 'kotor' secara sengaja,
untuk mendemonstrasikan proses pembersihan data (data cleaning).

Dataset ini disimpan ke data/sales_raw.csv
"""
import csv
import random
from datetime import datetime, timedelta

random.seed(42)  # agar hasil bisa direproduksi (NFR-04 di charter)

produk = [
    ("Kopi Susu", 18000),
    ("Teh Tarik", 12000),
    ("Roti Bakar", 15000),
    ("Nasi Goreng", 25000),
    ("Es Jeruk", 10000),
    ("Mie Ayam", 20000),
    ("Croissant", 22000),
    ("Smoothie Bowl", 35000),
]
kota = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Medan"]

rows = []
start = datetime(2025, 1, 1)

for i in range(500):
    tanggal = start + timedelta(days=random.randint(0, 180))
    nama, harga = random.choice(produk)
    qty = random.randint(1, 8)

    # Sengaja membuat data 'kotor':
    # 1. Beberapa tanggal pakai format berbeda
    if random.random() < 0.15:
        tgl_str = tanggal.strftime("%d/%m/%Y")      # format 01/01/2025
    else:
        tgl_str = tanggal.strftime("%Y-%m-%d")      # format 2025-01-01

    # 2. Beberapa nama kota tidak konsisten (huruf besar/spasi)
    kt = random.choice(kota)
    if random.random() < 0.1:
        kt = kt.upper()
    if random.random() < 0.05:
        kt = " " + kt + " "

    # 3. Beberapa qty hilang (kosong)
    qty_val = "" if random.random() < 0.06 else qty

    rows.append([tgl_str, nama, kt, harga, qty_val])

# 4. Tambahkan beberapa baris duplikat
for _ in range(20):
    rows.append(random.choice(rows[:480]))

# Tulis ke CSV
with open("integrated-tech-portfolio/day-02-data-science/data/sales_raw.csv",
          "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["tanggal", "produk", "kota", "harga_satuan", "jumlah"])
    w.writerows(rows)

print(f"Dataset dibuat: {len(rows)} baris (termasuk duplikat & data kotor)")
