
harga_normal = 50000

usia = int(input("Masukkan usia: "))

if usia < 12:
    status_pelajar = "tidak"
    hari_nonton = input("Masukkan hari nonton: ")
else:
    status_pelajar = input("Apakah anda pelajar SMA dengan kartu pelajar (ya/tidak): ")
    hari_nonton = input("Masukkan hari nonton: ")

# DISKON
diskon = 0

# CEK KONDISI DISKON
if usia >= 1 and usia < 12:
    if 50 > diskon:
        diskon = 50

if status_pelajar == "ya" and usia >= 12: 
    if 30 > diskon:
        diskon = 30

if hari_nonton == "selasa":
    if 20 > diskon:
        diskon = 20  

# menghitung seluruh jumlah
harga_diskon = harga_normal - (diskon / 100 * harga_normal)

# hasil
if diskon == 0:
    print("Maaf, anda tidak dapat diskon")
else:
    print(f"Diskon anda sebesar: {diskon}%")
    print(f"Total yang harus anda bayar: Rp.{harga_diskon}")
