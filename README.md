Berikut adalah versi yang lebih rinci dengan tambahan informasi yang relevan:

---

# **Aplikasi Kriptografi: Vigenere, Playfair, dan Hill Cipher**

Aplikasi ini dirancang untuk mengenkripsi dan mendekripsi pesan menggunakan tiga metode kriptografi klasik, yang sangat berguna dalam memahami konsep dasar keamanan informasi. Algoritma yang diimplementasikan adalah:
1. **Vigenere Cipher**: Menggunakan metode substitusi multi-alfabet untuk mengenkripsi pesan.
2. **Playfair Cipher**: Cipher berbasis digraph yang beroperasi dengan menggunakan tabel 5x5.
3. **Hill Cipher**: Menggunakan aljabar matriks (matriks 3x3 dalam program ini) untuk enkripsi berbasis linear.

## **Persyaratan Sistem**
- **Python 3.x**: Program ini dikembangkan menggunakan Python 3, jadi pastikan versi yang digunakan adalah versi terbaru Python 3.
- **NumPy Library**: Untuk mendukung operasi aljabar matriks dalam Hill Cipher, program ini memerlukan pustaka NumPy.

## **Instalasi dan Persiapan**
1. **Clone Repositori**: Salin repositori dari GitHub ke komputer lokal Anda dengan perintah:
   ```bash
   git clone https://github.com/username/repository-name.git
   ```

2. **Navigasi ke Folder Program**: Arahkan terminal atau command prompt ke direktori project:
   ```bash
   cd Kriptografi
   ```

3. **Instalasi NumPy**: Jika Anda belum menginstal NumPy, jalankan perintah ini untuk menginstalnya:
   ```bash
   pip install numpy
   ```

## **Menjalankan Aplikasi**
Setelah semua dependensi terinstal, Anda bisa menjalankan program dengan perintah berikut:
```bash
python main.py
```
Atau jika menggunakan Python 3:
```bash
python3 main.py
```
GUI (Graphical User Interface) aplikasi akan terbuka dan Anda bisa mulai menggunakan fitur enkripsi dan dekripsi.

## **Fitur-Fitur Utama**
- **Enkripsi Pesan**: Menggunakan salah satu dari tiga metode kriptografi yang tersedia.
- **Dekripsi Pesan**: Dekripsi pesan terenkripsi dengan kunci yang sama.
- **Input File**: Pengguna dapat memuat teks dari file eksternal yang ingin dienkripsi atau didekripsi.
- **Simpan Hasil**: Hasil enkripsi atau dekripsi dapat disimpan ke file teks.
- **Antarmuka Pengguna yang Ramah**: Aplikasi menggunakan antarmuka berbasis GUI yang mudah digunakan dengan elemen seperti text area, tombol, dan input key.

### **Cara Menggunakan Program**
1. **Input Pesan**: Ketik atau muat pesan teks yang ingin Anda enkripsi atau dekripsi melalui antarmuka.
2. **Masukkan Kunci**: Kunci minimal 12 karakter diperlukan untuk keamanan yang lebih baik.
3. **Pilih Cipher**: Tentukan metode enkripsi yang Anda inginkan (Vigenere, Playfair, atau Hill).
4. **Enkripsi**: Klik tombol "Encrypt" untuk mengenkripsi teks yang dimasukkan.
5. **Dekripsi**: Klik tombol "Decrypt" untuk mengubah ciphertext kembali menjadi plaintext.
6. **Menyimpan dan Membuka File**: Buka file teks atau simpan hasil enkripsi ke dalam file baru.

## **Perhatian Saat Menggunakan**
- **Kunci pada Hill Cipher**: Pastikan bahwa kunci yang digunakan untuk Hill Cipher adalah matriks invertible (memiliki invers) agar proses dekripsi dapat berjalan dengan benar.
- **Panjang Kunci**: Untuk keamanan yang lebih baik, terutama pada Vigenere Cipher, panjang kunci yang lebih besar dari teks yang dienkripsi sangat dianjurkan.
- **Format Pesan**: Program secara otomatis menghapus spasi dan mengubah huruf menjadi kapital sebelum melakukan enkripsi.

## **Struktur File Program**
- **main.py**: File ini berisi seluruh logika antarmuka pengguna dan menghubungkan metode kriptografi yang diimplementasikan di modul terpisah.
- **vigenere.py**: Modul ini mengandung algoritma enkripsi dan dekripsi untuk Vigenere Cipher.
- **playfair.py**: Mengimplementasikan enkripsi dan dekripsi Playfair Cipher.
- **hillcipher.py**: Modul untuk Hill Cipher yang memanfaatkan operasi matriks 3x3.
- **readme.md**: Dokumentasi yang memberikan panduan penggunaan aplikasi ini.

## **Contoh Input dan Output**
Misalnya, jika Anda ingin mengenkripsi teks **"HELLO WORLD"** dengan kunci **"SECURITYISKEY"** menggunakan Vigenere Cipher, hasilnya mungkin akan tampak seperti:
- **Ciphertext**: "ZOLSGKOPISFH"

## **Kesimpulan**
Aplikasi ini memberikan pemahaman mendalam tentang konsep enkripsi dan dekripsi menggunakan metode klasik. Program ini sangat cocok untuk pengguna yang ingin belajar lebih dalam tentang kriptografi klasik, atau bahkan untuk mereka yang tertarik dalam membangun aplikasi serupa di masa mendatang.

---

