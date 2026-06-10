"""
hardened_app.py
Versi SmartData Platform yang DIPERKUAT KEAMANANNYA.

Ini adalah app.py dari DAY 4 + perbaikan dari temuan audit (DAY 5):
  F-01: rate limiting sederhana
  F-02: security headers
  F-03: validasi input
  F-04: error handling yang aman (tidak membocorkan detail)

Menunjukkan kemampuan menerjemahkan TEMUAN AUDIT menjadi KODE yang lebih aman.
"""
import json
import os
import time
from collections import defaultdict
from flask import Flask, jsonify, request

app = Flask(__name__)

SUMMARY_PATH = os.environ.get("SUMMARY_PATH", "summary.json")

# ------------------------------------------------------------
# F-01: Rate limiting sederhana (tanpa dependensi eksternal)
# Membatasi jumlah permintaan per IP dalam jendela waktu.
# ------------------------------------------------------------
RATE_LIMIT = 30          # maksimal 30 permintaan
WINDOW = 60              # per 60 detik
_riwayat = defaultdict(list)


def kena_rate_limit(ip):
    sekarang = time.time()
    # buang catatan lama
    _riwayat[ip] = [t for t in _riwayat[ip] if sekarang - t < WINDOW]
    if len(_riwayat[ip]) >= RATE_LIMIT:
        return True
    _riwayat[ip].append(sekarang)
    return False


# ------------------------------------------------------------
# F-02: Security headers pada setiap respons
# ------------------------------------------------------------
@app.after_request
def tambah_security_headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Referrer-Policy"] = "no-referrer"
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    return resp


# ------------------------------------------------------------
# F-01: Cek rate limit sebelum memproses permintaan
# ------------------------------------------------------------
@app.before_request
def cek_rate_limit():
    ip = request.remote_addr or "unknown"
    if kena_rate_limit(ip):
        return jsonify({"error": "Terlalu banyak permintaan. Coba lagi nanti."}), 429


def load_summary():
    try:
        with open(SUMMARY_PATH, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "total_pendapatan": 45062000, "total_transaksi": 499,
            "produk_terlaris": "Smoothie Bowl", "kota_tertinggi": "Surabaya",
            "pendapatan_per_produk": {"Smoothie Bowl": 10360000, "Es Jeruk": 2680000},
        }


@app.route("/api/insight")
def api_insight():
    data = load_summary()
    produk = data["pendapatan_per_produk"]
    terlemah = min(produk, key=produk.get)
    return jsonify({
        "ringkasan": f"Total Rp {data['total_pendapatan']:,} dari {data['total_transaksi']} transaksi.",
        "rekomendasi": [
            f"Andalkan {data['produk_terlaris']}.",
            f"Evaluasi {terlemah}.",
        ],
    })


# ------------------------------------------------------------
# F-03: Contoh endpoint dengan validasi input
# ------------------------------------------------------------
@app.route("/api/echo")
def echo():
    pesan = request.args.get("pesan", "")
    # Validasi: panjang & karakter
    if len(pesan) > 100:
        return jsonify({"error": "Input terlalu panjang (maks 100 karakter)."}), 400
    # Sanitasi sederhana: buang karakter berisiko
    bersih = "".join(c for c in pesan if c.isalnum() or c in " .,!?-")
    return jsonify({"echo": bersih})


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


# ------------------------------------------------------------
# F-04: Error handler yang tidak membocorkan detail internal
# ------------------------------------------------------------
@app.errorhandler(500)
def server_error(e):
    # Detail asli di-log di server, pengguna hanya lihat pesan umum
    app.logger.error(f"Internal error: {e}")
    return jsonify({"error": "Terjadi kesalahan internal."}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # F-04: debug=False di produksi
    app.run(host="0.0.0.0", port=port, debug=False)
