# Scope & Requirements — SmartData Platform

## 1. Scope Statement

SmartData Platform akan dibangun secara bertahap. Setiap fase punya batas yang jelas agar project tidak melebar (*scope creep*).

### In-Scope (Dikerjakan)
- Pengumpulan & pembersihan data dari sumber publik.
- Analisis data deskriptif & visualisasi.
- Fitur AI: ringkasan/insight otomatis berbasis prompt.
- Deployment ke cloud (free-tier).
- Kontrol keamanan dasar (autentikasi, manajemen secret, prinsip least-privilege).
- Antarmuka web sederhana untuk menampilkan hasil.

### Out-of-Scope (Tidak Dikerjakan)
- Real-time streaming data berskala besar.
- Model machine learning custom yang dilatih dari nol.
- Multi-region cloud architecture.
- Sertifikasi keamanan formal (mis. ISO 27001).

---

## 2. Functional Requirements (Apa yang sistem LAKUKAN)

| ID | Requirement | Fase |
|----|-------------|------|
| FR-01 | Sistem dapat memuat dataset dari file CSV. | DAY 2 |
| FR-02 | Sistem dapat membersihkan & meringkas data. | DAY 2 |
| FR-03 | Sistem dapat menghasilkan insight via AI. | DAY 3 |
| FR-04 | Sistem dapat diakses online. | DAY 4 |
| FR-05 | Akses sistem terlindungi & data sensitif aman. | DAY 5 |
| FR-06 | Pengguna dapat melihat hasil lewat web. | DAY 6 |

## 3. Non-Functional Requirements (Bagaimana sistem BERPERILAKU)

| ID | Requirement |
|----|-------------|
| NFR-01 | **Keterbacaan:** kode & dokumen mudah dipahami orang lain. |
| NFR-02 | **Keamanan:** tidak ada kredensial yang ter-hardcode. |
| NFR-03 | **Biaya:** seluruh project berjalan di tier gratis. |
| NFR-04 | **Reproducibility:** orang lain bisa menjalankan ulang dari README. |

---

## 4. Deliverables per Fase

- **DAY 1:** Dokumen perencanaan (charter, scope, roadmap, risk). ✅
- **DAY 2:** Notebook analisis + dataset bersih.
- **DAY 3:** Script/aplikasi AI insight.
- **DAY 4:** Aplikasi ter-deploy + URL.
- **DAY 5:** Laporan keamanan + perbaikan.
- **DAY 6:** Antarmuka web final.
