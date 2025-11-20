kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("\nDaftar kontak masih kosong!")
        return
    print("\n=== DAFTAR KONTAK ===")
    for nama, info in kontak.items():
        print(f"Nama : {nama}")
        print(f"Nomor : {info[0]}")
        print(f"Email : {info[1]}")
        print("------------------------")

def cari_kontak():
    email = input("Masukkan email kontak yang dicari: ").lower()
    for nama, info in kontak.items():
        if info[1] == email:
            print("\nKontak ditemukan:")
            print(f"Nama : {nama}")
            print(f"Nomor : {info[0]}")
            print(f"Email : {info[1]}")
            return
    print("Kontak tidak ditemukan")

def tambah_kontak():
    nama = input("Masukkan nama kontak baru: ").lower()
    if nama in kontak:
        print("Kontak sudah ada!")
        return
    nomor = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ").lower()
    while "@gmail.com" not in email:
        print("Email harus mengandung @gmail.com")
        email = input("Masukkan email: ").lower()
    kontak[nama] = [nomor, email]
    print("\nKontak berhasil ditambahkan!")

def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui: ").lower()
    if nama not in kontak:
        print("Kontak tidak ditemukan!")
        return
    email_baru = input("Masukkan email baru: ").lower()
    while "@gmail.com" not in email_baru:
        print("Email harus mengandung @gmail.com")
        email_baru = input("Masukkan email baru: ").lower()
    kontak[nama][1] = email_baru
    print("\nEmail berhasil diperbarui!")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").lower()
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan!")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")