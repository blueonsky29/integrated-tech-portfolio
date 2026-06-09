# DAY 4 — Cloud Computing: Deploy ke AWS

**Bidang:** Cloud Computing / AWS (Fundamental → Intermediate)
**Output:** Aplikasi web yang membungkus AI Advisor + dokumentasi arsitektur & deployment AWS.

---

## 🎯 Tujuan Hari Ini

Membawa SmartData Platform dari "jalan di laptop" menjadi "bisa diakses siapa saja lewat internet". Saya berperan sebagai *Cloud Engineer* yang:

1. Membungkus AI Advisor (DAY 3) menjadi **aplikasi web** (Flask).
2. Meng-*containerize*-nya dengan **Docker**.
3. Mendokumentasikan **arsitektur AWS** untuk deployment.

Memenuhi requirement dari DAY 1:
- **FR-04** — sistem dapat diakses online

> 🔗 **Keterkaitan:** DAY 3 menghasilkan logika AI. DAY 4 membungkusnya jadi web app dengan endpoint API, lalu menyiapkannya untuk cloud. Platform mulai terasa seperti produk nyata.

---

## 🌐 Aplikasi Web

Aplikasi Flask dengan 3 endpoint:

| Endpoint | Fungsi |
|----------|--------|
| `GET /` | Dashboard visual (HTML) |
| `GET /api/insight` | Insight dalam format JSON (untuk integrasi) |
| `GET /health` | Health check untuk monitoring cloud |

Aplikasi ini **benar-benar berjalan** — bisa kamu coba lokal sekarang juga.

---

## ☁️ Sisi Cloud (AWS)

Dua dokumen penting:
- **`docs/architecture.md`** — diagram & penjelasan layanan AWS (Route 53, Load Balancer, App Runner/ECS, S3, Secrets Manager, CloudWatch) beserta alasan pemilihannya.
- **`deploy/deployment-guide.md`** — langkah deploy ke AWS App Runner, plus opsi lokal & Docker.

> 💡 **Pendekatan jujur:** dokumentasi deployment menunjukkan saya paham *konsep* cloud (arsitektur, biaya, keamanan) tanpa harus mengeluarkan biaya nyata. Aplikasinya sendiri tetap bisa di-demo gratis secara lokal/Docker.

---

## 📂 Isi Folder

```
day-04-cloud-aws/
├── README.md
├── app/
│   ├── app.py             ← aplikasi web Flask
│   ├── requirements.txt
│   └── Dockerfile         ← untuk containerization
├── docs/
│   └── architecture.md    ← arsitektur AWS + diagram
└── deploy/
    └── deployment-guide.md ← langkah deploy step-by-step
```

---

## ▶️ Cara Mencoba (Lokal)

```bash
cd day-04-cloud-aws/app
pip install -r requirements.txt
python app.py
```

Buka `http://localhost:5000` → dashboard tampil. 🎉

---

## 🧠 Apa yang Saya Pelajari

- Mengubah script menjadi **web service** dengan endpoint API.
- **Containerization** (Docker): "jalan di mesin saya" → "jalan di mana saja".
- Konsep arsitektur cloud AWS & alasan memilih tiap layanan.
- Kesadaran **biaya** (Free Tier, billing alert) dan **keamanan** (Secrets Manager, HTTPS).
- Pentingnya **health check** untuk aplikasi cloud.

---

## ▶️ Selanjutnya

**DAY 5 — Cybersecurity:** mengaudit & mengamankan platform yang sudah ter-deploy ini — memeriksa kerentanan, menerapkan praktik keamanan, dan membuat laporan keamanan.
