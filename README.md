** APLIKASI NEWTON-RAPHSON (METODE NUMERIK)
 Dibuat dengan Python & Kivy GUI**


1. DESKRIPSI PROGRAM
Program ini adalah aplikasi berbasis GUI (Graphical User Interface) 
yang digunakan untuk mencari akar suatu persamaan non-linear 
menggunakan Metode Newton-Raphson.

Aplikasi ini dibuat menggunakan Python dengan framework Kivy, 
dan memanfaatkan Sympy untuk melakukan perhitungan matematika 
secara simbolik (turunan dan evaluasi fungsi).

Dengan aplikasi ini, pengguna bisa mengetik langsung persamaan 
matematika f(x), dan program akan:

- Menampilkan turunan otomatis f'(x) saat pengguna mengetik
- Menghitung akar menggunakan Metode Newton-Raphson
- Menampilkan hasil setiap iterasi dalam bentuk tabel yang rapi
- Menghentikan perhitungan otomatis jika hasil sudah konvergen 
  atau jika turunan bernilai nol


2. PENJELASAN METODE NEWTON-RAPHSON
Metode Newton-Raphson adalah salah satu metode numerik untuk mencari 
akar (root) dari sebuah persamaan non-linear f(x) = 0.

Artinya, kita ingin mencari nilai x yang membuat fungsi f(x) bernilai nol.

Metode ini menggunakan pendekatan turunan pertama fungsi 
untuk memperkirakan akar dengan cara berulang (iteratif).

RUMUS UMUM:
    x(i+1) = x(i) - f(x(i)) / f'(x(i))

PENJELASAN RUMUS:
    x(i)     : nilai tebakan awal akar
    f(x(i))  : nilai fungsi pada titik x(i)
    f'(x(i)) : turunan fungsi pada titik x(i)
    x(i+1)   : nilai perkiraan akar baru

Proses diulang hingga selisih |x(i+1) - x(i)| lebih kecil dari 
nilai toleransi (ε).

Metode ini sangat cepat jika nilai awal x0 cukup dekat dengan 
akar sebenarnya, namun bisa gagal jika:
    - Turunan f'(x) = 0
    - Fungsi tidak kontinu di sekitar akar
    - Nilai awal terlalu jauh dari akar sebenarnya


3. FITUR UTAMA PROGRAM
1. Input f(x)
   Pengguna bebas mengetik bentuk fungsi, misalnya:  x**3 - 4*x + 1

2. Turunan Otomatis
   Aplikasi langsung menampilkan hasil turunan f'(x) ketika pengguna 
   mengetik persamaan.

3. Input Parameter Perhitungan:
   - Nilai awal x₀
   - Nilai toleransi ε
   - Jumlah iterasi maksimum n

4. Tombol "Hitung Akar"
   Menjalankan proses Newton-Raphson dan menampilkan hasil per iterasi.

5. Tabel Hasil Iterasi:
   - Iterasi ke-
   - Nilai xᵢ
   - Nilai f(xᵢ)
   - Nilai f'(xᵢ)
   - Selisih |xᵢ₊₁ - xᵢ|

6. Deteksi Kesalahan Otomatis:
   - Input tidak valid
   - Turunan bernilai nol
   - Fungsi tidak konvergen

7. Desain Warna Pastel:
   Tampilan lembut dan menarik dengan kombinasi warna pink & ungu pastel.


4. PENJELASAN STRUKTUR KODE
a. Bagian Import Library
   Program menggunakan:
   - kivy.app, kivy.uix.*    → untuk antarmuka (tombol, input, layout)
   - sympy                   → untuk menghitung turunan & evaluasi fungsi
   - Window.clearcolor       → untuk memberi warna dasar aplikasi

b. Kelas BoxLabel
   Kelas khusus yang membuat label dengan kotak berwarna,
   agar tampilannya seragam dengan input box.

c. Kelas NewtonLayout
   Kelas utama yang mengatur seluruh tata letak (layout) aplikasi:
   - Bagian input persamaan dan parameter
   - Label turunan otomatis
   - Tombol "Hitung Akar"
   - Area hasil (tabel iterasi)

d. Fungsi update_derivative()
   Berfungsi menampilkan hasil turunan f'(x) secara otomatis setiap 
   kali pengguna mengetik di kolom f(x).

e. Fungsi hitung()
   Menjalankan langkah-langkah utama metode Newton-Raphson:
   - Membaca input
   - Mengubah fungsi ke bentuk matematis
   - Menghitung nilai f(x) dan f'(x)
   - Melakukan iterasi hingga konvergen atau batas iterasi tercapai
   - Menampilkan hasil di tabel


5. KELEBIHAN PROGRAM
- Antarmuka sederhana dan interaktif
- Turunan otomatis tanpa perlu input manual
- Hasil langsung tampil dalam bentuk tabel
- Warna lembut (pink & ungu pastel) yang nyaman dilihat
- Cocok untuk pembelajaran atau demonstrasi metode numerik di kelas

DIBUAT UNTUK: 
   Tugas UTS Praktikum Komputasi Numerik
   Topik: Metode Newton-Raphson (Versi Dinamis & Otomatis)

DIBUAT OLEH:
   [Kelompok 1]
Nama Anggota :
- Abdi Dzil Ikram (2408107010024)
- Aulia Lutfi (2408107010033)
- Annisa Rahma Fathia (2408107010027)
- Dara Ramadhani (2408107010028)
- Putroe Fatimah Azzahra (2408107010002)
