# DAY 6 — Web Development: Dashboard & GitHub Pages

**Bidang:** Web Development (Fundamental → Intermediate)
**Output:** Dashboard web statis (HTML/CSS/JS) yang bisa di-host gratis & live.

---

## 🎯 Tujuan Hari Ini

Membuat **lapisan presentasi final** — antarmuka web yang menyatukan seluruh perjalanan
DAY 1–5 menjadi satu halaman yang bisa dilihat siapa saja. Saya berperan sebagai *Web Developer*
yang membangun dashboard ringan tanpa framework, lalu mempublikasikannya via **GitHub Pages**.

Memenuhi requirement dari DAY 1:
- **FR-06** — pengguna dapat melihat hasil lewat web

> 🔗 **Keterkaitan:** ini adalah penutup yang menyatukan semuanya. Dashboard menampilkan
> keenam modul sebagai satu sistem koheren — persis visi "satu produk utuh" dari DAY 1.

---

## 🎨 Tentang Dashboard

Halaman tunggal (`index.html`) dengan:
- **Hero** bergaya "ruang kontrol sistem" dengan indikator status live.
- **Pipeline visual** menampilkan alur 6 fase platform.
- **Kartu modul** untuk tiap DAY (di-render dengan JavaScript).
- **Statistik cakupan** teknis.
- **Bagian Tentang** dengan link ke repository.

Dibuat dengan **HTML + CSS + JavaScript murni** — tanpa framework, tanpa dependensi.
Ringan, cepat, dan mudah di-host.

---

## 📂 Isi Folder

```
day-06-web/
├── README.md
├── index.html      ← dashboard lengkap (satu file)
└── assets/         ← (untuk gambar/ikon tambahan bila perlu)
```

---

## 🌐 Cara Publikasi ke GitHub Pages (Gratis!)

Ini bagian seru: portofolio kamu akan punya **alamat web sungguhan**.

1. Buka repo `integrated-tech-portfolio` di GitHub.
2. Klik **Settings → Pages** (menu kiri).
3. Di bagian **Source**, pilih **Deploy from a branch**.
4. Pilih branch **main**, folder **/ (root)** → **Save**.
5. Tunggu ~1 menit. GitHub memberi URL seperti:
   `https://blueonsky29.github.io/integrated-tech-portfolio/`

> ⚠️ Karena `index.html` ada di dalam folder `day-06-web/`, akses dashboard di:
> `https://blueonsky29.github.io/integrated-tech-portfolio/day-06-web/`
>
> **Atau** (lebih rapi): salin `index.html` ke root repo agar langsung tampil di URL utama.

---

## ▶️ Cara Mencoba (Lokal)

Cukup buka file `index.html` dengan browser (klik dua kali). Tidak perlu server.

---

## 🧠 Apa yang Saya Pelajari

- Membuat layout responsif dengan **CSS Grid & Flexbox**.
- Menggunakan **CSS custom properties** (variabel) untuk tema konsisten.
- **Render dinamis** konten dengan JavaScript (array → kartu).
- Prinsip desain: hierarki visual, tipografi, whitespace.
- **Deployment statis** lewat GitHub Pages (hosting gratis).
- Aksesibilitas dasar: `prefers-reduced-motion`, kontras warna.

---

## 🎉 Penutup Portofolio

Dengan DAY 6, SmartData Platform lengkap sebagai **satu sistem utuh**:

```
Perencanaan → Data → AI → Cloud → Keamanan → Web
   DAY 1      DAY 2  DAY 3  DAY 4    DAY 5     DAY 6
```

Setiap fase membangun di atas fase sebelumnya, persis seperti yang direncanakan
di project charter DAY 1. Portofolio ini menunjukkan bukan hanya skill teknis di
banyak domain, tapi kemampuan **menghubungkannya menjadi sesuatu yang koheren** —
hal yang membedakan seorang profesional dari sekadar pengikut tutorial.
