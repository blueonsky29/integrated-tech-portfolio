"""
ai_advisor.py
SmartData AI Advisor — mengubah ringkasan data (DAY 2) menjadi
insight bisnis berbahasa natural.

DUA MODE:
  1. rule-based  : jalan tanpa API key (gratis, untuk demo)
  2. llm         : pakai OpenAI/Azure OpenAI bila API key tersedia

Memenuhi requirement DAY 1:
  - FR-03: sistem menghasilkan insight via AI

Keamanan (mengantisipasi DAY 5):
  - API key TIDAK pernah ditulis di kode, dibaca dari environment variable
"""
import json
import os

BASE = "integrated-tech-portfolio/day-03-ai-engineering"
SUMMARY_PATH = "integrated-tech-portfolio/day-02-data-science/output/summary.json"


# ============================================================
# Muat ringkasan data dari DAY 2
# ============================================================
def load_summary():
    with open(SUMMARY_PATH, encoding="utf-8") as f:
        return json.load(f)


def format_rincian_produk(per_produk):
    baris = [f"  - {nama}: Rp {nilai:,}" for nama, nilai in per_produk.items()]
    return "\n".join(baris)


# ============================================================
# MODE 1 — Rule-based (tanpa API, selalu jalan)
# Logika sederhana yang meniru "penalaran" seorang analis.
# ============================================================
def generate_rule_based(data):
    produk = data["pendapatan_per_produk"]
    kota = data["pendapatan_per_kota"]

    terlaris = data["produk_terlaris"]
    terlemah = min(produk, key=produk.get)
    kota_kuat = data["kota_tertinggi"]
    kota_lemah = min(kota, key=kota.get)

    selisih_kota = kota[kota_kuat] - kota[kota_lemah]

    insight = f"""## 📊 Analisis Penjualan (Rule-Based)

**Ringkasan:**
Usahamu mencatat total pendapatan Rp {data['total_pendapatan']:,} dari
{data['total_transaksi']} transaksi (rata-rata Rp {data['rata_per_transaksi']:,}/transaksi).

**3 Rekomendasi:**

1. **Andalkan produk juara.** "{terlaris}" adalah penyumbang pendapatan terbesar
   (Rp {produk[terlaris]:,}). Pastikan stok bahannya selalu tersedia dan
   pertimbangkan membuat varian/paket dari produk ini.

2. **Evaluasi produk lemah.** "{terlemah}" menyumbang paling sedikit
   (Rp {produk[terlemah]:,}). Coba promosi bundling dengan produk laris,
   atau pertimbangkan mengganti menu jika terus stagnan.

3. **Pemerataan wilayah.** {kota_kuat} adalah pasar terkuat, sementara
   {kota_lemah} terlemah (selisih Rp {selisih_kota:,}). Alokasikan promosi
   lebih banyak di {kota_lemah} untuk menyeimbangkan pertumbuhan.
"""
    return insight


# ============================================================
# MODE 2 — LLM (OpenAI / Azure OpenAI)
# Hanya jalan jika API key tersedia di environment variable.
# ============================================================
def generate_llm(data):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None  # tidak ada key -> fallback ke rule-based

    try:
        from openai import OpenAI
    except ImportError:
        print("   (paket 'openai' belum terpasang — pakai: pip install openai)")
        return None

    client = OpenAI(api_key=api_key)

    system_prompt = (
        "Kamu adalah konsultan bisnis untuk UMKM di Indonesia. "
        "Beri analisis dan maksimal 3 rekomendasi yang praktis, "
        "berbahasa Indonesia sederhana, tanpa jargon. "
        "Jawab HANYA berdasarkan data yang diberikan, jangan mengarang angka."
    )

    user_prompt = f"""Berikut ringkasan penjualan usaha saya:
- Total pendapatan: Rp {data['total_pendapatan']:,}
- Jumlah transaksi: {data['total_transaksi']}
- Produk terlaris: {data['produk_terlaris']}
- Kota tertinggi: {data['kota_tertinggi']}

Rincian per produk:
{format_rincian_produk(data['pendapatan_per_produk'])}

Beri analisis singkat dan 3 rekomendasi konkret."""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
    )
    return "## 🤖 Analisis Penjualan (AI / LLM)\n\n" + resp.choices[0].message.content


# ============================================================
# MAIN
# ============================================================
def main():
    data = load_summary()
    print("Data dari DAY 2 berhasil dimuat.\n")

    # Coba LLM dulu, fallback ke rule-based
    hasil = generate_llm(data)
    mode = "LLM (OpenAI/Azure)"
    if hasil is None:
        hasil = generate_rule_based(data)
        mode = "Rule-Based (tanpa API)"

    print(f"Mode yang dipakai: {mode}")
    print("=" * 55)
    print(hasil)

    # Simpan hasil
    with open(f"{BASE}/output/insight.md", "w", encoding="utf-8") as f:
        f.write(f"<!-- Dihasilkan dengan mode: {mode} -->\n\n")
        f.write(hasil)
    print("=" * 55)
    print(f"\nInsight disimpan ke: {BASE}/output/insight.md")


if __name__ == "__main__":
    main()
