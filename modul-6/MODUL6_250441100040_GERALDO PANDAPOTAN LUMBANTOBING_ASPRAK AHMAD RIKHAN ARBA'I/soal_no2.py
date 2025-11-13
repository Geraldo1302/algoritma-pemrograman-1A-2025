def ubah_ke_tuple(teks):
    angka = ""
    hasil = []
    for ch in teks + ",":
        if ch != ",":
            angka += ch
        else:
            if angka != "":
                hasil.append(int(angka))
                angka = ""
    return tuple(hasil)

t1_input = input("Masukkan angka-angka tuple 1 (pisahkan dengan koma): ")
t1 = ubah_ke_tuple(t1_input)

t2_input = input("Masukkan angka-angka tuple 2 (pisahkan dengan koma): ")
t2 = ubah_ke_tuple(t2_input)

gabung = t1 + t2

unik = []
for x in gabung:
    if x not in unik:
        unik.append(x)

hasil = []
for angka in unik:
    pos = 0
    while pos < len(hasil) and hasil[pos] > angka:
        pos += 1
    hasil.insert(pos, angka)

hasil_akhir = tuple(hasil)

print("Hasil akhir:", hasil_akhir)
