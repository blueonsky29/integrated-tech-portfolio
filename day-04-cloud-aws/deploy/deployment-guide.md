# Panduan Deployment — SmartData Platform ke AWS

Panduan ini menjelaskan cara men-deploy aplikasi ke AWS menggunakan **AWS App Runner**
(cara termudah untuk container). Disusun agar bisa diikuti pemula.

> ⚠️ **Catatan biaya:** selalu cek Free Tier & pasang billing alert sebelum mulai.
> Untuk sekadar belajar, kamu juga bisa menjalankan aplikasi secara lokal (lihat bagian akhir).

---

## Opsi A — Deploy ke AWS App Runner (Cloud)

### 1. Siapkan container image
- Pastikan file `app/Dockerfile`, `app/app.py`, dan `app/requirements.txt` sudah ada.
- Push kode ke repository (GitHub) — App Runner bisa langsung connect ke GitHub.

### 2. Buat layanan App Runner
1. Buka **AWS Console → App Runner → Create service**
2. Source: pilih **Source code repository** → hubungkan ke GitHub repo kamu
3. Pilih branch `main`, folder `day-04-cloud-aws/app`
4. Build: App Runner mendeteksi `Dockerfile` otomatis
5. Port: isi **5000**
6. Klik **Create & Deploy**

### 3. Selesai
- App Runner memberi URL publik seperti `https://xxxx.awsapprunner.com`
- Akses URL → dashboard SmartData Platform tampil.

### 4. Pasang billing alert (WAJIB)
- **AWS Budgets → Create budget** → set alert di angka kecil (mis. $1).

---

## Opsi B — Jalankan Lokal (Gratis, untuk demo)

```bash
cd day-04-cloud-aws/app
pip install -r requirements.txt

# jalankan dengan server produksi:
gunicorn --bind 0.0.0.0:5000 app:app

# atau cara sederhana:
python app.py
```

Buka browser ke `http://localhost:5000`.

---

## Opsi C — Jalankan dengan Docker (lokal)

```bash
cd day-04-cloud-aws/app
docker build -t smartdata .
docker run -p 5000:5000 smartdata
```

---

## ✅ Verifikasi Berhasil

| Endpoint | Hasil yang diharapkan |
|----------|----------------------|
| `/` | Dashboard HTML tampil |
| `/api/insight` | Respons JSON berisi insight |
| `/health` | `{"status": "ok"}` |

---

## 🧠 Yang Ditunjukkan dari Deployment Ini

- Memahami perbedaan **server dev vs produksi** (gunicorn).
- **Containerization** dengan Docker (jalan sama di mana saja).
- Konsep **health check** untuk monitoring cloud.
- Kesadaran **biaya** dan **keamanan** sejak tahap deploy.
