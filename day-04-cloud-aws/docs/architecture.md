# Arsitektur Cloud — SmartData Platform di AWS

Dokumen ini menjelaskan bagaimana SmartData Platform di-deploy ke AWS,
beserta alasan pemilihan setiap layanan. Tujuannya menunjukkan pemahaman
**konsep arsitektur cloud**, bukan sekadar menjalankan perintah.

---

## 🗺️ Diagram Arsitektur

```
                    Internet (Pengguna)
                          │
                          ▼
            ┌─────────────────────────────┐
            │   Amazon Route 53 (DNS)     │   ← alamat domain
            └──────────────┬──────────────┘
                           ▼
            ┌─────────────────────────────┐
            │  Application Load Balancer  │   ← bagi trafik, HTTPS
            └──────────────┬──────────────┘
                           ▼
            ┌─────────────────────────────┐
            │   Amazon ECS / App Runner   │   ← jalankan container app
            │   (container dari Dockerfile)│
            └──────────────┬──────────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
   ┌──────────────────┐      ┌────────────────────┐
   │  Amazon S3       │      │  AWS Secrets Mgr    │
   │  (data & file)   │      │  (API key aman)     │
   └──────────────────┘      └────────────────────┘
              │
              ▼
   ┌──────────────────┐
   │  Amazon CloudWatch│     ← log & monitoring
   └──────────────────┘
```

---

## 🧱 Layanan yang Digunakan & Alasannya

| Layanan AWS | Fungsi | Kenapa dipilih |
|-------------|--------|----------------|
| **Route 53** | DNS / domain | Mengarahkan domain ke aplikasi |
| **Application Load Balancer** | Membagi trafik + HTTPS | Skalabilitas & keamanan koneksi |
| **ECS / App Runner** | Menjalankan container | App Runner paling sederhana untuk container tunggal |
| **Amazon S3** | Menyimpan data & file statis | Murah, tahan lama, terintegrasi |
| **Secrets Manager** | Menyimpan API key | Tidak ada kredensial di kode (lihat R-03) |
| **CloudWatch** | Log & monitoring | Memantau kesehatan aplikasi |

---

## 💰 Pertimbangan Biaya (Free Tier)

Sesuai risk register DAY 1 (**R-02: biaya cloud tak terduga**):

- Gunakan **AWS Free Tier** untuk semua layanan saat belajar.
- Pasang **billing alert** di AWS Budgets (mis. alert bila > $1).
- Matikan resource saat tidak dipakai.
- **App Runner** punya skala-ke-nol sehingga hemat saat idle.

---

## 🔐 Keamanan (mengantisipasi DAY 5)

- API key disimpan di **Secrets Manager**, bukan di kode atau environment file.
- Load Balancer memaksa **HTTPS** (koneksi terenkripsi).
- Prinsip **least privilege** pada IAM Role: aplikasi hanya boleh akses S3 & Secrets yang dibutuhkan.

---

## 🔗 Keterkaitan Antar-Hari

- **DAY 3** menghasilkan AI Advisor → DAY 4 membungkusnya jadi web app & men-deploy-nya.
- **DAY 5** akan mengamankan arsitektur ini lebih dalam.
- **DAY 6** akan menyempurnakan antarmuka web yang sudah live.
