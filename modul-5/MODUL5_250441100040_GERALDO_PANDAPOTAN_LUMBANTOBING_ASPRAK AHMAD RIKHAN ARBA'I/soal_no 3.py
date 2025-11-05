def gaji_bersih(nama, jabatan, gaji_pokok):
    if jabatan.lower() == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan.lower() == "staff":
        tunjangan = gaji_pokok * 0.05
    else:   
        tunjangan = 0
    # PAJAK
    pajak = gaji_pokok * 0.05

    gaji_bersih = gaji_pokok + tunjangan - pajak

    print(f"Nama        : {nama}")
    print(f"Jabatan     : {jabatan}")
    print(f"Gaji Pokok  : Rp {gaji_pokok}")
    print(f"Tunjangan   : Rp {tunjangan}")
    print(f"Pajak (5%)  : Rp {pajak}")
    print(f"Gaji Bersih : Rp {gaji_bersih}")

nama = input("Nama Karyawan: ")
jabatan = input("Jabatan (Manager/Staff): ")
gaji_pokok = float(input("gaji pokok: "))

gaji_bersih(nama, jabatan, gaji_pokok)