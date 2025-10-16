beras = 12000
gula = 14000
minyak = 20000

while True:
    barang_pilihan =input("pilih jenis barang (beras, gula, minyak, cukup) :")
    if barang_pilihan == "beras":
        jumlah_barang = int(input("masukkan jumlah barang :"))
        harga_beras = beras * jumlah_barang
        print(f"harga dari berasnya sebesar Rp.{harga_beras}")
    if barang_pilihan == "gula":
        jumlah_barang = int(input("masukkan jumlah barang :"))
        harga_gula = gula * jumlah_barang
        print(f"harga dari gulanya sebesar Rp.{harga_gula}")
    if barang_pilihan == "minyak":
        jumlah_barang = int(input("masukkan jumlah barang :"))
        harga_minyak = minyak * jumlah_barang
        print(f"harga dati minyak sebesar : {harga_minyak}")
    if barang_pilihan == "cukup":
        total_harga = harga_beras + harga_gula + harga_minyak