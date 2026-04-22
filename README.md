# **Sistem Manajemen Kasir Sembako**

Program kasir berbasis CLI (Command Line Interface) yang dibuat menggunakan Python untuk memenuhi tugas UAS Pemrograman. Aplikasi ini memiliki dua mode utama, yaitu mode Admin untuk pengelolaan stok dan mode Kasir untuk proses transaksi.

## **Fitur Utama**

**1. Mode Admin**

Digunakan untuk mengelola inventaris barang sebelum melakukan penjualan. Fitur yang tersedia:

 - Manajemen Barang: Tambah barang baru, ubah harga, dan hapus barang dari daftar.
 - Keamanan: Dilengkapi sistem login dengan batas maksimal 3 kali percobaan sebelum akun dikunci.
 - Stok & Harga: Pembaruan data harga dan ketersediaan stok secara real-time di dalam dictionary.

**2. Mode Kasir**,
Digunakan untuk melayani transaksi pelanggan. Fitur yang tersedia:

 - Pemilihan Kasir: Memilih identitas kasir yang bertugas sebelum memulai transaksi.
 - Cek Stok Otomatis: Program akan menolak input jika jumlah belanja melebihi stok yang tersedia.
 - Sistem Diskon Otomatis: * Belanja >= Rp 100.000 mendapatkan diskon 10%.
 - Belanja >= Rp 50.000 mendapatkan diskon 5%.
 - Struk Transaksi: Menampilkan ringkasan total belanja, potongan harga, dan nominal akhir yang harus dibayar.

## **Struktur Data**

Program ini memanfaatkan beberapa struktur data Python:

 - Dictionary: Untuk menyimpan data sembako (harga & stok), data diskon, dan kredensial admin.
 - List: Untuk menyimpan daftar nama kasir yang terdaftar.
 - Match-Case & Functions: Menggunakan modularitas fungsi untuk memisahkan logika login, menu admin, dan perhitungan kasir.

## **Cara Menjalankan**
 - Pastikan Python sudah terinstall di perangkat Anda.
 - Clone atau download file UAS_python_Kasir.py.
 - Buka terminal atau command prompt di folder tersebut.
 - Jalankan perintah:
   ```python UAS_python_Kasir.py```
 - Pilih mode (admin/kasir) dan ikuti instruksi yang muncul di layar.

## Preview Program

### Mode Admin
<img width="257" height="220" alt="image" src="https://github.com/user-attachments/assets/5a8ce04c-8a21-498a-b63b-994703e5265c" />

### Mode Kasir
<img width="448" height="591" alt="image" src="https://github.com/user-attachments/assets/2c6b8e7a-ffe9-4862-bff5-60353965f2d9" />

