jumlah_baris = int(input("masukkan jumlah baris lampu :"))
for baris in range(1, jumlah_baris + 1):
    baris_lampu = int(input(f"masukkan jumlah lampu pada baris ke-{baris}:"))
    kali = baris_lampu // 5
    sisa = baris_lampu % 5

    for ulang in range(kali):
        nomor_lampu = ulang * 5 + 1
        print(f"lampu ke-{nomor_lampu} pada baris {baris} berkedip.")
        print(f"lampu ke-{nomor_lampu + 1} pada baris {baris} berkedip - kedip.")
        print(f"lampu ke-{nomor_lampu + 2} pada baris {baris} berkedip.")
        print(f"lampu ke-{nomor_lampu + 3} pada baris {baris} berkedip - kedip.")
        print(f"lampu ke-{nomor_lampu + 4} pada baris {baris} menyala.")

    for cek in range(baris, baris_lampu + 1):
        if cek == baris_lampu:
            print("periksa sambungan utama .")
    print()