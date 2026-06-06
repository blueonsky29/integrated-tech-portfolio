# Risk Register — SmartData Platform

Daftar risiko yang mungkin muncul selama project, beserta cara mengatasinya. Mengelola risiko *sebelum* terjadi adalah ciri Project Manager yang matang.

**Skala:** Probabilitas (Rendah/Sedang/Tinggi) × Dampak (Rendah/Sedang/Tinggi)

---

| ID | Risiko | Probabilitas | Dampak | Mitigasi (Pencegahan) | Kontingensi (Jika terjadi) |
|----|--------|--------------|--------|----------------------|---------------------------|
| R-01 | Dataset publik tidak tersedia / berkualitas buruk | Sedang | Tinggi | Pilih 2-3 sumber cadangan sejak awal | Gunakan dataset sintetis |
| R-02 | Melebihi batas free-tier cloud (biaya tak terduga) | Sedang | Tinggi | Set billing alert; pakai layanan gratis | Hentikan resource; pindah ke alternatif lokal |
| R-03 | Kredensial / API key bocor ke GitHub | Rendah | Tinggi | Gunakan `.gitignore` & environment variable | Rotasi/hapus key segera |
| R-04 | Scope melebar (scope creep) | Tinggi | Sedang | Patuhi dokumen scope; catat ide di backlog | Tunda fitur tambahan ke "versi 2" |
| R-05 | Waktu tidak cukup per fase | Sedang | Sedang | Pecah tiap DAY jadi tugas kecil | Kurangi cakupan fase, fokus inti |
| R-06 | Skill gap pada topik tertentu | Sedang | Sedang | Pelajari dasar dulu; mulai dari versi sederhana | Buat versi minimal yang tetap berfungsi |

---

## 🚨 Risiko Prioritas Tinggi

Tiga risiko yang paling perlu diawasi:

1. **R-03 (Kebocoran kredensial)** — paling berbahaya secara keamanan. Akan ditangani serius di DAY 5.
2. **R-02 (Biaya cloud)** — bisa menimbulkan tagihan nyata. Selalu cek free-tier sebelum deploy di DAY 4.
3. **R-04 (Scope creep)** — musuh utama setiap project. Dokumen scope adalah benteng pertahanannya.

---

## 📝 Cara Memakai Dokumen Ini

Tinjau ulang risk register ini di awal setiap fase. Tambahkan risiko baru saat ditemukan, dan tandai risiko yang sudah teratasi. Risk register adalah **dokumen hidup**, bukan sekali tulis lalu dilupakan.
