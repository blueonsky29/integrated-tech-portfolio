# Prompt Templates — SmartData AI Advisor

Dokumen ini berisi *prompt* yang dirancang untuk mengubah ringkasan data penjualan
menjadi insight bisnis. Ini adalah inti dari **prompt engineering**: bagaimana cara
"berbicara" dengan AI agar menghasilkan output yang berguna, konsisten, dan terstruktur.

---

## 1. System Prompt (menetapkan peran AI)

```
Kamu adalah konsultan bisnis untuk UMKM (Usaha Mikro, Kecil, Menengah) di Indonesia.
Tugasmu menganalisis data penjualan dan memberi rekomendasi yang:
- Praktis dan bisa langsung diterapkan pemilik usaha kecil
- Menggunakan bahasa Indonesia yang sederhana, bukan jargon
- Fokus pada peningkatan pendapatan dan efisiensi
- Ringkas: maksimal 3 rekomendasi utama

Jawab HANYA berdasarkan data yang diberikan. Jangan mengarang angka.
```

## 2. User Prompt Template (menyisipkan data)

```
Berikut ringkasan penjualan usaha saya selama periode berjalan:

- Total pendapatan: Rp {total_pendapatan}
- Jumlah transaksi: {total_transaksi}
- Rata-rata per transaksi: Rp {rata_per_transaksi}
- Produk terlaris: {produk_terlaris}
- Kota dengan penjualan tertinggi: {kota_tertinggi}

Rincian pendapatan per produk:
{rincian_produk}

Tolong berikan analisis singkat dan 3 rekomendasi konkret untuk meningkatkan usaha saya.
```

---

## 🧠 Prinsip Prompt Engineering yang Diterapkan

| Prinsip | Penerapan |
|---------|-----------|
| **Role-setting** | Memberi AI peran "konsultan UMKM" agar jawaban relevan |
| **Constraint** | Membatasi maksimal 3 rekomendasi → output fokus |
| **Grounding** | "Jawab HANYA berdasarkan data" → mencegah halusinasi |
| **Format control** | Meminta bahasa sederhana, bukan jargon |
| **Context injection** | Menyisipkan angka asli dari `summary.json` |

> Prinsip-prinsip ini adalah fondasi bekerja dengan layanan seperti
> **Azure OpenAI Service** atau **OpenAI API**.
