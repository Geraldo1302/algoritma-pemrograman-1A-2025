inventaris = {}

def tampilkan_semua():
    if not inventaris:
        print("Inventaris kosong.")
    else:
        print("\nDaftar Barang:")
        for id_barang, data in inventaris.items():
            print(f"ID: {id_barang}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

def cari_barang():
    id_barang = input("Masukkan ID barang: ")
    if id_barang in inventaris:
        nama, harga, stok = inventaris[id_barang]
        print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
    else:
        print("Barang tidak ditemukan.")

def tambah_barang(): 
    id_barang = input("Masukkan ID barang baru: ")
    if id_barang in inventaris:
        print("ID sudah ada!") 
        return
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan.")

def update_stok():
    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
        return

    tambah = int(input("Masukkan perubahan stok (boleh negatif): "))
    stok_baru = inventaris[id_barang][2] + tambah

    if stok_baru < 0:
        print("Stok tidak boleh negatif!")
        return

    inventaris[id_barang][2] = stok_baru
    print("Stok berhasil diperbarui.")

def hapus_barang():
    id_barang = input("Masukkan ID barang yang akan dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

while True:
    print("\n=== MENU INVENTARIS ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stok")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")