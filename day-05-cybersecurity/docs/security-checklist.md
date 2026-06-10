# Security Checklist — SmartData Platform

Daftar periksa keamanan praktis yang diterapkan & diverifikasi. Bisa dipakai ulang
untuk project lain. Berbasis prinsip umum (OWASP, praktik cloud).

---

## 🔐 Manajemen Secret
- [x] API key & password tidak ter-hardcode di kode
- [x] Secret dibaca dari environment variable
- [x] File `.env` diblokir oleh `.gitignore`
- [x] Tersedia `.env.example` sebagai template (tanpa nilai asli)
- [x] Diverifikasi otomatis dengan `security_scan.py`

## 🌐 Keamanan Aplikasi Web
- [x] Security headers (X-Content-Type-Options, X-Frame-Options, CSP)
- [x] Rate limiting untuk mencegah penyalahgunaan
- [x] Validasi panjang & tipe input
- [x] Sanitasi input dari karakter berisiko
- [x] Mode debug dimatikan (`debug=False`) di produksi
- [x] Pesan error tidak membocorkan detail internal

## ☁️ Keamanan Cloud (Infrastruktur)
- [x] Secret disimpan di AWS Secrets Manager (bukan di kode)
- [x] HTTPS dipaksa di level Load Balancer
- [x] Prinsip least privilege pada IAM Role
- [x] Monitoring & log via CloudWatch
- [x] Billing alert untuk mencegah penyalahgunaan biaya

## 🤖 Keamanan AI (relevan dengan AI Advisor)
- [x] Prompt diberi instruksi "jawab hanya berdasarkan data" (kurangi halusinasi)
- [x] API key LLM dikelola sebagai secret
- [ ] *(lanjutan)* Filter output AI sebelum ditampilkan ke pengguna
- [ ] *(lanjutan)* Batasi panjang & biaya panggilan LLM

## 👤 Perlindungan Data Pribadi
- [x] Tidak menyimpan data pribadi sensitif tanpa alasan
- [x] Data agregat (ringkasan), bukan data individu, yang diproses AI
- [ ] *(lanjutan)* Enkripsi data saat istirahat (at-rest) bila menyimpan data sensitif

---

> Tanda `[ ]` adalah langkah lanjutan yang relevan saat platform berkembang.
> Keamanan adalah proses berkelanjutan — checklist ini ditinjau ulang setiap perubahan besar.
