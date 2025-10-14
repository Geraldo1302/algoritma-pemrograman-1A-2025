while True:
    nama = input("Masukkan nama pembeli: ")

    total = 0
    daftar_nama = ""
    daftar_harga = ""

    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' jika sudah): ")
        if barang.lower()== "selesai":
            break
        harga = int(input("Masukkan harga barang: "))
        daftar_nama = daftar_nama + barang + "\n"
        daftar_harga = daftar_harga + "Rp" + str(harga) + "\n"
        total = total + harga

    print("\n====== Struk Pembelian ======")
    print("Daftar Barang:")
    print(daftar_nama)
    print("Daftar Harga:")
    print(daftar_harga)
    print("Total Harga  : Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut == "n":
        print("Program selesai. Terima kasih!")
        break
