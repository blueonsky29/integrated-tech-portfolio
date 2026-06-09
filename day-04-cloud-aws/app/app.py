"""
app.py
SmartData Platform — Web API & Dashboard
Membungkus AI Advisor (DAY 3) menjadi aplikasi web yang bisa di-deploy ke cloud.

Memenuhi requirement DAY 1:
  - FR-04: sistem dapat diakses online

Endpoint:
  GET  /            -> dashboard sederhana (HTML)
  GET  /api/insight -> insight dalam format JSON
  GET  /health      -> health check (dipakai cloud untuk cek aplikasi hidup)
"""
import json
import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Path ke ringkasan data dari DAY 2
SUMMARY_PATH = os.environ.get(
    "SUMMARY_PATH",
    "../day-02-data-science/output/summary.json"
)


def load_summary():
    """Memuat ringkasan data. Bila file tak ada, pakai data contoh."""
    try:
        with open(SUMMARY_PATH, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Data cadangan agar aplikasi tetap jalan di cloud
        return {
            "total_pendapatan": 45062000,
            "total_transaksi": 499,
            "rata_per_transaksi": 90304,
            "produk_terlaris": "Smoothie Bowl",
            "kota_tertinggi": "Surabaya",
            "pendapatan_per_produk": {"Smoothie Bowl": 10360000, "Nasi Goreng": 8125000},
            "pendapatan_per_kota": {"Surabaya": 9905000, "Jakarta": 7807000},
        }


def generate_insight(data):
    """Versi ringkas dari AI Advisor (rule-based) untuk web."""
    produk = data["pendapatan_per_produk"]
    terlaris = data["produk_terlaris"]
    terlemah = min(produk, key=produk.get)
    return {
        "ringkasan": (
            f"Total pendapatan Rp {data['total_pendapatan']:,} "
            f"dari {data['total_transaksi']} transaksi."
        ),
        "rekomendasi": [
            f"Andalkan produk juara: {terlaris} (Rp {produk[terlaris]:,}).",
            f"Evaluasi produk lemah: {terlemah} (Rp {produk[terlemah]:,}).",
            f"Fokus pemasaran di luar {data['kota_tertinggi']} untuk pemerataan.",
        ],
    }


DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SmartData Platform</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 800px; margin: 40px auto;
           padding: 0 20px; background: #0f172a; color: #e2e8f0; }
    h1 { color: #60a5fa; }
    .card { background: #1e293b; border-radius: 12px; padding: 24px; margin: 16px 0; }
    .stat { font-size: 28px; font-weight: bold; color: #34d399; }
    ul { line-height: 1.8; }
    .badge { background: #2563eb; color: white; padding: 4px 10px;
             border-radius: 6px; font-size: 12px; }
  </style>
</head>
<body>
  <h1>🚀 SmartData Platform</h1>
  <span class="badge">Live on Cloud</span>
  <div class="card">
    <h2>📊 Ringkasan</h2>
    <p class="stat">Rp {{ total }}</p>
    <p>{{ ringkasan }}</p>
  </div>
  <div class="card">
    <h2>💡 Rekomendasi AI</h2>
    <ul>
      {% for r in rekomendasi %}<li>{{ r }}</li>{% endfor %}
    </ul>
  </div>
  <div class="card">
    <small>API endpoint: <code>/api/insight</code> · Health: <code>/health</code></small>
  </div>
</body>
</html>
"""


@app.route("/")
def dashboard():
    data = load_summary()
    insight = generate_insight(data)
    return render_template_string(
        DASHBOARD_HTML,
        total=f"{data['total_pendapatan']:,}",
        ringkasan=insight["ringkasan"],
        rekomendasi=insight["rekomendasi"],
    )


@app.route("/api/insight")
def api_insight():
    data = load_summary()
    return jsonify(generate_insight(data))


@app.route("/health")
def health():
    """Health check — cloud platform memanggil ini untuk cek aplikasi hidup."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # host 0.0.0.0 agar bisa diakses dari luar container (penting untuk cloud)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
