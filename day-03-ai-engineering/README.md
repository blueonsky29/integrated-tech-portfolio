# DAY 3 — AI Engineering: SmartData AI Advisor

**Bidang:** AI Engineering / Prompt Engineering (Fundamental → Intermediate)
**Output:** Generator insight bisnis berbasis AI yang membaca data dari DAY 2.

---

## 🎯 Tujuan Hari Ini

Memberi "otak" pada SmartData Platform. Saya berperan sebagai *AI Engineer* yang membangun **AI Advisor**: sistem yang membaca ringkasan data penjualan (`summary.json` dari DAY 2) dan mengubahnya menjadi **rekomendasi bisnis berbahasa natural**.

Memenuhi requirement dari DAY 1:
- **FR-03** — sistem menghasilkan insight via AI

> 🔗 **Keterkaitan antar-hari:** DAY 2 menghasilkan angka. DAY 3 mengubah angka itu menjadi *saran yang bisa ditindaklanjuti*. Inilah lompatan dari "data" ke "kecerdasan".

---

## 🧩 Dua Mode (Desain Cerdas)

Sistem ini punya dua mode yang otomatis dipilih:

| Mode | Kapan dipakai | Kelebihan |
|------|---------------|-----------|
| **Rule-Based** | Saat tidak ada API key | Gratis, selalu jalan, bisa di-demo siapa saja |
| **LLM (OpenAI/Azure)** | Saat API key tersedia | Insight lebih kaya & natural |

> 💡 **Kenapa dua mode?** Portofolio harus bisa dijalankan siapa pun tanpa biaya. Tapi saya juga ingin menunjukkan kemampuan *prompt engineering* dengan LLM sungguhan. Dua mode menjawab keduanya — sebuah keputusan desain yang sadar trade-off.

---

## 🔐 Catatan Keamanan (mengantisipasi DAY 5)

- API key **tidak pernah** ditulis di dalam kode.
- Key dibaca dari *environment variable* (`OPENAI_API_KEY`).
- File `.env.example` disediakan sebagai template; file `.env` asli diblokir oleh `.gitignore`.

Ini adalah praktik keamanan standar industri yang akan diperdalam di DAY 5.

---

## 📂 Isi Folder

```
day-03-ai-engineering/
├── README.md
├── ai_advisor.py           ← program utama (dua mode)
├── requirements.txt
├── .env.example            ← template konfigurasi (TANPA key asli)
├── prompts/
│   └── prompt_templates.md ← rancangan prompt (inti prompt engineering)
└── output/
    └── insight.md          ← contoh hasil insight
```

---

## ▶️ Cara Menjalankan

**Mode rule-based (tanpa biaya):**
```bash
cd day-03-ai-engineering
python ai_advisor.py
```

**Mode LLM (dengan OpenAI):**
```bash
pip install -r requirements.txt
# set API key dulu (jangan tulis di kode!):
export OPENAI_API_KEY="sk-..."     # Mac/Linux
python ai_advisor.py
```

---

## 🧠 Apa yang Saya Pelajari

- **Prompt engineering**: role-setting, constraint, grounding, format control (lihat `prompts/prompt_templates.md`)
- Cara memanggil **LLM API** (OpenAI/Azure OpenAI) dengan aman
- Pentingnya **fallback** agar sistem tetap berjalan tanpa dependensi eksternal
- Mengelola **secret/API key** dengan environment variable, bukan hardcode

---

## ▶️ Selanjutnya

**DAY 4 — Cloud Computing (AWS):** men-deploy AI Advisor ini agar bisa diakses online lewat URL, bukan hanya di komputer lokal.
