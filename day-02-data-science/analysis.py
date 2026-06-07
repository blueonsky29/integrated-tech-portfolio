"""
analysis.py
Membersihkan dan menganalisis data penjualan UMKM untuk SmartData Platform.

Memenuhi requirement dari DAY 1:
  - FR-01: memuat dataset dari CSV
  - FR-02: membersihkan & meringkas data

Alur: Load -> Clean -> Analyze -> Visualize -> Export
"""
import pandas as pd
import matplotlib.pyplot as plt

BASE = "integrated-tech-portfolio/day-02-data-science"

# ============================================================
# 1. LOAD — memuat data mentah (FR-01)
# ============================================================
df = pd.read_csv(f"{BASE}/data/sales_raw.csv")
print("=" * 50)
print("1. DATA MENTAH")
print(f"   Jumlah baris awal : {len(df)}")
print(f"   Kolom             : {list(df.columns)}")
print(f"   Nilai kosong      :\n{df.isnull().sum().to_string()}")

# ============================================================
# 2. CLEAN — membersihkan data (FR-02)
# ============================================================
print("\n" + "=" * 50)
print("2. PEMBERSIHAN DATA")

# 2a. Hapus duplikat
sebelum = len(df)
df = df.drop_duplicates()
print(f"   Duplikat dihapus  : {sebelum - len(df)} baris")

# 2b. Normalkan nama kota (hapus spasi, samakan kapitalisasi)
df["kota"] = df["kota"].str.strip().str.title()
print(f"   Kota dinormalkan  : {sorted(df['kota'].unique())}")

# 2c. Samakan format tanggal (tangani dua format sekaligus)
df["tanggal"] = pd.to_datetime(df["tanggal"], format="mixed", dayfirst=True)
print(f"   Rentang tanggal   : {df['tanggal'].min().date()} s/d {df['tanggal'].max().date()}")

# 2d. Tangani qty yang hilang -> isi dengan median (lebih tahan outlier)
kosong = df["jumlah"].isnull().sum()
df["jumlah"] = pd.to_numeric(df["jumlah"], errors="coerce")
median_qty = df["jumlah"].median()
df["jumlah"] = df["jumlah"].fillna(median_qty).astype(int)
print(f"   Qty kosong diisi  : {kosong} baris -> median ({int(median_qty)})")

# 2e. Buat kolom turunan: total pendapatan per transaksi
df["pendapatan"] = df["harga_satuan"] * df["jumlah"]
print(f"   Kolom baru        : 'pendapatan' (harga x jumlah)")
print(f"   Baris akhir bersih: {len(df)}")

# Simpan data bersih
df.to_csv(f"{BASE}/data/sales_clean.csv", index=False)

# ============================================================
# 3. ANALYZE — meringkas insight (FR-02)
# ============================================================
print("\n" + "=" * 50)
print("3. RINGKASAN INSIGHT")

total_pendapatan = df["pendapatan"].sum()
total_transaksi = len(df)
rata_transaksi = df["pendapatan"].mean()

per_produk = df.groupby("produk")["pendapatan"].sum().sort_values(ascending=False)
per_kota = df.groupby("kota")["pendapatan"].sum().sort_values(ascending=False)
per_bulan = df.groupby(df["tanggal"].dt.to_period("M"))["pendapatan"].sum()

print(f"   Total pendapatan  : Rp {total_pendapatan:,.0f}")
print(f"   Total transaksi   : {total_transaksi}")
print(f"   Rata-rata/transaksi: Rp {rata_transaksi:,.0f}")
print(f"   Produk terlaris   : {per_produk.index[0]} (Rp {per_produk.iloc[0]:,.0f})")
print(f"   Kota tertinggi    : {per_kota.index[0]} (Rp {per_kota.iloc[0]:,.0f})")

# ============================================================
# 4. VISUALIZE — membuat grafik
# ============================================================
plt.style.use("seaborn-v0_8-darkgrid")

# Grafik 1: pendapatan per produk
fig, ax = plt.subplots(figsize=(10, 5))
per_produk.plot(kind="barh", ax=ax, color="#2563eb")
ax.set_title("Pendapatan per Produk", fontsize=14, fontweight="bold")
ax.set_xlabel("Pendapatan (Rp)")
plt.tight_layout()
plt.savefig(f"{BASE}/output/pendapatan_per_produk.png", dpi=120)
plt.close()

# Grafik 2: tren pendapatan bulanan
fig, ax = plt.subplots(figsize=(10, 5))
per_bulan.plot(kind="line", marker="o", ax=ax, color="#16a34a", linewidth=2)
ax.set_title("Tren Pendapatan Bulanan", fontsize=14, fontweight="bold")
ax.set_ylabel("Pendapatan (Rp)")
ax.set_xlabel("Bulan")
plt.tight_layout()
plt.savefig(f"{BASE}/output/tren_bulanan.png", dpi=120)
plt.close()

print("\n   Grafik disimpan ke folder output/")

# ============================================================
# 5. EXPORT — simpan ringkasan untuk DAY 3 (AI)
# ============================================================
ringkasan = {
    "total_pendapatan": int(total_pendapatan),
    "total_transaksi": int(total_transaksi),
    "rata_per_transaksi": int(rata_transaksi),
    "produk_terlaris": per_produk.index[0],
    "kota_tertinggi": per_kota.index[0],
    "pendapatan_per_produk": per_produk.astype(int).to_dict(),
    "pendapatan_per_kota": per_kota.astype(int).to_dict(),
}

import json
with open(f"{BASE}/output/summary.json", "w", encoding="utf-8") as f:
    json.dump(ringkasan, f, indent=2, ensure_ascii=False)

print("   Ringkasan disimpan: output/summary.json (input untuk DAY 3 - AI)")
print("\n" + "=" * 50)
print("SELESAI. Data siap dipakai untuk fase AI (DAY 3).")
