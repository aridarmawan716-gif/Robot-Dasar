# Robot-Dasar 🤖

Proyek ini adalah sistem kontrol robot sederhana yang dijalankan melalui **Termux** di Android. Program menggunakan bahasa Python untuk mengirim perintah ke mikrokontroler melalui komunikasi Serial.

## Fitur
* Kendali arah (Maju, Mundur, Berhenti).
* Komunikasi Serial via kabel OTG.
* Ringan dan bisa dijalankan langsung dari smartphone.

## Cara Penggunaan
1. Pastikan `pyserial` sudah terinstal: `pip install pyserial`.
2. Hubungkan mikrokontroler ke HP menggunakan kabel OTG.
3. Jalankan program:
   ```bash
   python robot_control.py
   

### 3. Simpan dan Keluar
*   Tekan `CTRL + O`, lalu `Enter` untuk menyimpan.
*   Tekan `CTRL + X` untuk keluar.

### 4. Kirim ke GitHub
Sekarang, jalankan urutan perintah Git seperti yang kamu lakukan di **Screenshot_2026-05-10-03-31-32-09.jpg**:
```bash
git add README.md
git commit -m "Menambahkan file README.md"
git push
