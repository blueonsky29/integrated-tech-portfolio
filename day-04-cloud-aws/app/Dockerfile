# Dockerfile — mengemas SmartData Platform menjadi container
# Container membuat aplikasi berjalan sama di mana saja (lokal maupun cloud).

FROM python:3.11-slim

WORKDIR /app

# Install dependencies dulu (memanfaatkan cache Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi
COPY . .

# Port yang diekspos
EXPOSE 5000

# Jalankan dengan gunicorn (server produksi, bukan server dev Flask)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
