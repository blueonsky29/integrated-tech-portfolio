# DAY 5 — Cybersecurity: Audit & Hardening

**Bidang:** Cybersecurity (Fundamental → Intermediate)
**Output:** Audit keamanan + pemindai defensif + aplikasi yang diperkuat + checklist.

---

## 🎯 Tujuan Hari Ini

Mengamankan platform yang sudah dibangun (DAY 1–4). Saya berperan sebagai *Security Analyst*
yang melakukan **audit defensif**: menemukan kelemahan pada sistem sendiri, lalu memperbaikinya
sebelum penyerang menemukannya (*shift-left security*).

Memenuhi requirement dari DAY 1:
- **FR-05** — akses sistem terlindungi & data sensitif aman

> 🔗 **Keterkaitan:** seluruh fase sebelumnya menjadi objek audit. DAY 5 menutup risiko
> **R-03 (kebocoran kredensial)** dari risk register DAY 1.

---

## 🛡️ Pendekatan: Defensif, Bukan Ofensif

Portofolio ini mengambil sudut pandang **bertahan (blue team)**:
- Mengaudit & memperkuat sistem milik sendiri.
- TIDAK membuat alat untuk menyerang sistem orang lain.

Ini adalah sikap profesional yang tepat dan menunjukkan etika keamanan yang baik.

---

## 📂 Isi Folder

```
day-05-cybersecurity/
├── README.md
├── scripts/
│   ├── security_scan.py    ← pemindai defensif (cek secret, debug mode, dll)
│   └── hardened_app.py     ← aplikasi DAY 4 versi diperkuat
└── docs/
    ├── security-audit.md    ← laporan audit lengkap (temuan + risiko)
    └── security-checklist.md ← checklist keamanan yang bisa dipakai ulang
```

---

## 🔍 Apa yang Dilakukan

### 1. Pemindaian Otomatis (`security_scan.py`)
Memindai seluruh kode untuk menemukan: secret ter-hardcode, mode debug aktif,
password tertulis. Hasil: ✅ kode bersih (berkat praktik baik sejak DAY 3).

```bash
cd day-05-cybersecurity/scripts
SCAN_PATH=../.. python security_scan.py
```

### 2. Audit Manual (`security-audit.md`)
Mengidentifikasi 5 temuan (3 sedang, 2 rendah) dengan rekomendasi konkret.

### 3. Perbaikan Nyata (`hardened_app.py`)
Menerjemahkan temuan audit menjadi kode yang lebih aman:

| Temuan | Perbaikan |
|--------|-----------|
| Tidak ada rate limiting | Pembatasan 30 permintaan/menit per IP |
| Header keamanan kosong | X-Frame-Options, CSP, nosniff, dll |
| Input tidak divalidasi | Validasi panjang + sanitasi karakter |
| Error terlalu detail | Pesan umum + log di sisi server |

Semua perbaikan **sudah diuji dan berfungsi**.

---

## 🧠 Apa yang Saya Pelajari

- Konsep **shift-left security**: menemukan masalah sedini mungkin.
- Praktik keamanan aplikasi web (OWASP): headers, rate limiting, validasi input.
- Manajemen secret yang benar (memverifikasi, bukan sekadar percaya).
- Etika keamanan: fokus **bertahan**, bukan menyerang.
- Menerjemahkan **temuan audit → perbaikan kode** nyata.

---

## ▶️ Selanjutnya

**DAY 6 — Web / Network:** menyempurnakan antarmuka web platform sebagai lapisan
presentasi final yang menyatukan seluruh perjalanan.
