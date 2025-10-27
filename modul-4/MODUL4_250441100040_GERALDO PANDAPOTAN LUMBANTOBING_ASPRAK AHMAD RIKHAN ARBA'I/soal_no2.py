total_gaji = 0
total_lembur = 0
total_bonus = 0
gaji = 100000

for hari in range(1, 8):
    print(f"Hari ke-{hari}")
    jam = int(input("Masukkan jam lembur : "))
    if jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam = 0

    shift = input("Apakah shift malam? (y/n): ").lower()

    # Hitung lembur
    if 1 <= jam <= 3:
        lembur = jam * 25000
    elif jam == 4:
        lembur = 100000
    elif jam == 6:
        lembur = 200000
    elif jam == 8:
        lembur = 300000
    else:
        lembur = 0

    # Bonus shift malam
    if shift == "y":
        bonus = 50000  
    else:
        bonus = 0

    # Total
    total_harian = gaji + lembur + bonus
    total_gaji += total_harian
    total_lembur += jam
    total_bonus += bonus

print("\n=== Rekap Mingguan ===")
print("Total jam lembur:", total_lembur, "jam")
print("Total bonus shift malam: Rp", total_bonus)
print("Total gaji seminggu: Rp", total_gaji)