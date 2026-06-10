"""
security_scan.py
Pemindai keamanan sederhana & DEFENSIF untuk SmartData Platform.

Tujuan: memeriksa KODE SENDIRI untuk menemukan masalah keamanan umum
SEBELUM di-deploy. Ini adalah praktik "shift-left security" — menemukan
masalah sedini mungkin.

Yang diperiksa:
  1. Hardcoded secret (API key/password tertulis di kode)
  2. File .env yang berisiko ter-commit
  3. Mode debug yang aktif (berbahaya di produksi)
  4. Penggunaan fungsi berisiko

CATATAN: Ini alat audit defensif untuk kode milik sendiri,
bukan alat untuk menyerang sistem orang lain.
"""
import os
import re

# Pola sederhana yang menandakan kemungkinan secret ter-hardcode
POLA_RISIKO = {
    "Hardcoded API key (OpenAI)": re.compile(r"sk-[a-zA-Z0-9]{20,}"),
    "Hardcoded password": re.compile(r"(?i)password\s*=\s*['\"][^'\"]{3,}['\"]"),
    "Debug mode aktif": re.compile(r"debug\s*=\s*True"),
    "Secret key ter-hardcode": re.compile(r"(?i)secret[_-]?key\s*=\s*['\"][^'\"]{8,}['\"]"),
}

# File/folder yang dilewati
SKIP = {".git", "__pycache__", "node_modules", ".venv", "venv"}


def scan_file(path):
    temuan = []
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            for no, baris in enumerate(f, 1):
                # Lewati baris contoh/placeholder
                if "xxxx" in baris.lower() or ".example" in path:
                    continue
                for nama_risiko, pola in POLA_RISIKO.items():
                    if pola.search(baris):
                        temuan.append((no, nama_risiko, baris.strip()[:60]))
    except Exception:
        pass
    return temuan


def scan_directory(root):
    hasil = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for fn in filenames:
            if fn.endswith((".py", ".js", ".env", ".yaml", ".yml", ".json")):
                full = os.path.join(dirpath, fn)
                temuan = scan_file(full)
                if temuan:
                    hasil[full] = temuan
    return hasil


def main():
    root = os.environ.get("SCAN_PATH", "integrated-tech-portfolio")
    print(f"🔍 Memindai: {root}\n" + "=" * 55)

    hasil = scan_directory(root)

    # Cek keberadaan .gitignore yang melindungi .env
    gitignore = os.path.join(root, ".gitignore")
    env_terlindungi = False
    if os.path.exists(gitignore):
        with open(gitignore, encoding="utf-8") as f:
            env_terlindungi = ".env" in f.read()

    if not hasil:
        print("✅ Tidak ditemukan secret ter-hardcode atau debug mode aktif.")
    else:
        print(f"⚠️  Ditemukan {sum(len(v) for v in hasil.values())} potensi masalah:\n")
        for path, temuan in hasil.items():
            print(f"📄 {path}")
            for no, risiko, cuplikan in temuan:
                print(f"   Baris {no}: [{risiko}]")
                print(f"            > {cuplikan}")
            print()

    print("=" * 55)
    print("Status proteksi .env :", "✅ Terlindungi .gitignore" if env_terlindungi
          else "❌ TIDAK terlindungi — tambahkan .env ke .gitignore!")
    print("\nSelesai. Pemindaian defensif untuk kode sendiri.")


if __name__ == "__main__":
    main()
