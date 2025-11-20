kupon = {
    "DISKON10": 10,
    "HEMAT20": 20,
    "MURAH50": 50
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("\nDaftar kupon tersedia:")
        for kode, persen in kupon.items():
            print(f"{kode} = {persen}%")

def proses_transaksi():
    total = float(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon: ")

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * diskon / 100
        total_bayar = total - potongan

        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Potongan: Rp{potongan}")
        print(f"Total bayar: Rp{total_bayar}")

        del kupon[kode]
        print("Kupon berhasil digunakan dan dihapus.")
    else:
        print("Kupon tidak valid atau sudah digunakan.")

while True:
    print("\n=== MENU KUPON DISKON ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")