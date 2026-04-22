# ====DATA====
sembako = {
    "beras": [15000, 10],
    "gula": [13000, 8],
    "minyak": [20000, 5],
    "telur": [25000, 12],
    "mie": [3000, 20]
}

data_diskon = {
    100000: 0.10,   
    50000: 0.05    
}

admin = {
    "admin": "123",
    "asd": "qwe"
}

nama_kasir = ["faros","arya","zaki"]

#=== PROGRAM LOGIN ADMIN ====
def login_admin():
    percobaan = 0
    while percobaan < 3:
        username = input("Username admin: ")
        password = input("Password admin: ")
        if username in admin and password == admin[username]:
            print("\nLogin admin berhasil!\n")
            return True
        else:
            percobaan += 1
            print("Username atau password salah.")
            if percobaan == 3:
                print("Akun admin dikunci. Program berhenti, akun anda diblokir selama 30 menit")
                return False

#==== MAIN ADMIN ===
def menu_admin():
    while True:
        print("=== MENU ADMIN ===\n"
              "1. Lihat barang\n"
              "2. Tambah barang\n"
              "3. Ubah harga barang\n"
              "4. Hapus barang\n"
              "5. Keluar")
        
        pilih = input("Pilih menu (1-5): ")

        if pilih == "1":
            print("\n=== DAFTAR BARANG ===")
            for nama in sembako:
                print("-", nama, "= Rp", sembako[nama])
            konfirmasi = input("Apakah anda ingin ke MENU atau KELUAR? (m/k): ")
            if konfirmasi == "m":
                print("Kembali ke menu admin.")
            elif konfirmasi == "k":
              print("\nKeluar dari program.")
              break
            else:
              print("tidak valid.")
              break
                
        elif pilih == "2":
            nama = input("Nama barang: ")
            harga = int(input("Harga: "))
            sembako[nama] = harga
            print("Barang ditambahkan.")
        
        elif pilih == "3":
            nama = input("Nama barang yang akan diubah: ")
            if nama in sembako:
                sembako[nama] = int(input("Harga baru: "))
                print("Barang diubah.")
            else:
                print("Barang tidak ditemukan.")
        
        elif pilih == "4":
            nama = input("Nama barang yang dihapus: ")
            if nama in sembako:
                del sembako[nama]
                print("Barang dihapus.")
            else:
                print("Barang tidak ditemukan.")
        
        elif pilih == "5":
            konfirmasi = input("Apakah Anda ingin logout? (y/n): ")
            if konfirmasi == "y":
                print("\nLogout berhasil.")
                break
            else:
                print("Kembali ke menu admin.")
        else:
            print("Pilihan tidak valid.")

#==== login kasir ====
def login_kasir():
    print("Daftar Kasir:")
    for nama in nama_kasir:
        print("-", nama)
    
    kasir_aktif = input("Masukkan nama kasir: ")
    if kasir_aktif not in nama_kasir:
        print("Kasir tidak ditemukan.")
        kasir_aktif = nama_kasir[0]
    
    print("\nKasir aktif:", kasir_aktif)
    return kasir_aktif

#==== PROGRAM KASIR ====
def pilih_barang():
    print("=== DAFTAR SEMBAKO ===")
    for nama, data in sembako.items():
        print("-", nama, "= Rp", data[0], "| stok:", data[1])
    total = 0
    while True:
        barang = input("\nMasukkan nama barang (atau ketik 'selesai'): ")
        if barang == "selesai":
            break
        if barang in sembako:
            jumlah = int(input("Masukkan jumlah barang: "))
            if jumlah <= sembako[barang][1]:
                total += sembako[barang][0] * jumlah
                sembako[barang][1] -= jumlah
            else:
                print("Stok tidak cukup.")
        else:
            print("Barang tidak tersedia.")
    return total

def cek_diskon(total):
    diskon = 0
    for minimal in data_diskon:
        if total >= minimal and minimal > diskon:
            diskon = minimal
    if diskon == 0:
        return 0
    return data_diskon[diskon]

def menu_kasir(kasir_aktif):
    while True:
        total_belanja = pilih_barang()
        diskon = cek_diskon(total_belanja)
        potongan = total_belanja * diskon
        total_akhir = total_belanja - potongan

        print("\n====== STRUK ======")
        print("Kasir:", kasir_aktif)
        print("Total belanja sebelum diskon: Rp", format(total_belanja, ","))
        print("Diskon:", int(diskon * 100), "%", "(-Rp", format(int(potongan), ","), ")")
        print("Total yang harus dibayar: Rp", format(int(total_akhir), ","))
        print("\nTransaksi selesai. Kembali ke daftar sembako.\n")

#========================================= MAIN PROGRAM ==========================================

mode = input("Pilih Mode(kasir/admin): ")
match mode:
  case "kasir":
    kasir_aktif =login_kasir()
    menu_kasir(kasir_aktif)
  case "admin":
    if login_admin():
        menu_admin()