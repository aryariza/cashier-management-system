# Sistem Manajemen Kasir Sembako

Program kasir berbasis CLI (Command Line Interface) yang dibuat menggunakan Python untuk memenuhi tugas UAS Pemrograman. Aplikasi ini memiliki dua mode utama, yaitu mode Admin untuk pengelolaan stok dan mode Kasir untuk proses transaksi.

## Fitur Utama

### 1. Mode Admin
Digunakan untuk mengelola inventaris barang sebelum melakukan penjualan. Fitur yang tersedia:
- **Manajemen Barang:** Tambah barang baru, ubah harga, dan hapus barang dari daftar.
- **Keamanan:** Dilengkapi sistem login dengan batas maksimal 3 kali percobaan sebelum akun dikunci.
- **Stok & Harga:** Pembaruan data harga dan ketersediaan stok secara real-time di dalam dictionary.

### 2. Mode Kasir
Digunakan untuk melayani transaksi pelanggan secara efisien:
- **Pemilihan Kasir:** Memilih identitas kasir yang bertugas sebelum memulai transaksi.
- **Cek Stok Otomatis:** Program akan menolak input jika jumlah belanja melebihi stok yang tersedia.
- **Sistem Diskon Otomatis:** - Belanja >= **Rp 100.000** mendapatkan diskon **10%**.
  - Belanja >= **Rp 50.000** mendapatkan diskon **5%**.
- **Struk Transaksi:** Menampilkan ringkasan total belanja, potongan harga, dan nominal akhir yang harus dibayar.

## Struktur Data
Program ini memanfaatkan beberapa struktur data Python untuk efisiensi logika:
- **Dictionary:** Menyimpan data sembako (harga & stok), data diskon, dan kredensial admin.
- **List:** Menyimpan daftar nama kasir yang terdaftar.
- **Match-Case & Functions:** Menggunakan modularitas fungsi untuk memisahkan logika login, menu admin, dan perhitungan kasir.

## Cara Menjalankan
1. Pastikan Python sudah terinstall di perangkat Anda.
2. Clone atau download file `UAS_python_Kasir.py`.
3. Buka terminal atau command prompt di folder tersebut.
4. Jalankan perintah:
   ```bash
   python UAS_python_Kasir.py
