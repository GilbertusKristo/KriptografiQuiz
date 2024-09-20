# KriptografiQuiz
Berikut adalah format yang lebih variatif untuk dokumentasi program kriptografi:

---

# **Aplikasi Kriptografi: Vigenere, Playfair, dan Hill Cipher**

Aplikasi ini memungkinkan Anda untuk melakukan enkripsi dan dekripsi menggunakan tiga algoritma kriptografi populer:
1. **Vigenere Cipher**
2. **Playfair Cipher**
3. **Hill Cipher**

## **Persiapan Awal**
- Pastikan **Python 3** telah terinstal di sistem Anda. Jika belum, Anda bisa mengunduhnya dari [python.org](https://www.python.org/).

## **Langkah Instalasi**
1. Clone repositori ini ke komputer lokal Anda:
   ```bash
   git clone https://github.com/username/repository-name.git
   ```
2. Arahkan terminal atau command prompt ke folder project:
   ```bash
   cd KriptografiQuiz
   ```

### **Instalasi Dependensi**
Untuk menjalankan Hill Cipher, diperlukan pustaka **NumPy**. Anda bisa menginstalnya dengan menjalankan perintah berikut:
```bash
pip install numpy
```

## **Cara Menjalankan Program**
Setelah semuanya siap, jalankan program dengan perintah:
```bash
python main.py
```
Atau jika Anda menggunakan Python 3:
```bash
python3 main.py
```
Ini akan membuka antarmuka grafis di mana Anda bisa melakukan enkripsi dan dekripsi dengan mudah.

## **Panduan Penggunaan**
1. **Input Pesan**: Masukkan teks yang ingin Anda enkripsi atau dekripsi.
2. **Input Kunci**: Masukkan kunci dengan panjang minimal 12 karakter.
3. **Pilih Metode Cipher**: Tentukan metode kriptografi yang ingin digunakan (Vigenere, Playfair, atau Hill).
4. **Enkripsi**: Klik tombol *Encrypt* untuk mengenkripsi pesan yang dimasukkan.
5. **Dekripsi**: Klik tombol *Decrypt* untuk mendekripsi pesan yang telah dienkripsi.
6. **Simpan dan Muat File**: Anda juga dapat membuka file untuk melakukan enkripsi atau menyimpan hasil enkripsi ke file teks.

## **Struktur File Utama**
- **main.py**: File utama yang berisi logika antarmuka pengguna (GUI) serta menghubungkan berbagai cipher.
- **vigenere.py**: Mengandung implementasi algoritma Vigenere Cipher.
- **playfair.py**: Berisi algoritma Playfair Cipher.
- **hillcipher.py**: Mengimplementasikan Hill Cipher dengan matriks 3x3.

---

