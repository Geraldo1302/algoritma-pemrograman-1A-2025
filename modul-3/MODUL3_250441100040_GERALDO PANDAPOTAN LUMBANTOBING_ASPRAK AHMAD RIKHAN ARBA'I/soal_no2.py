print("Masukkan pin ATM anda 5 digit (XXYYY)")
print("XX = untuk NIM awal dan YYY = untuk NIM akhir ")
print("Maksimal 3 kali percobaan:\n")

pin_benar = 25040
benar = False
sisa_percobaan = 3

while sisa_percobaan > 0:
    pin_input = input("Masukkan pin (5 digit): ")

    angka = True
    for huruf in pin_input:
        if huruf < '0' or huruf > '9':
            angka = False

    hitung = 0
    for huruf in pin_input:
        hitung = hitung + 1

    if hitung != 5 or not angka:
        print(" PIN harus terdiri dari 5 angka! Silakan coba lagi.\n")
        continue  

    pin = int(pin_input)

    if pin == pin_benar:
        print("=" * 30)
        print(" PIN benar, akses diterima.")
        print("=" * 30)
        benar = True
        break
    else:
        sisa_percobaan = sisa_percobaan - 1
        if sisa_percobaan > 0:
            print(" PIN salah! Sisa percobaan:", sisa_percobaan, "\n")
        else:
            print(" PIN salah! Tidak ada percobaan tersisa.\n")

if not benar:
    print(" Akses ditolak, kartu diblokir.")
