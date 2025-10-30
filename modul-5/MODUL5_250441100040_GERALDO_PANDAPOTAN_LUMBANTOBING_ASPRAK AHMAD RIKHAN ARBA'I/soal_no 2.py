def cek_anagram(kata1, kata2):
    
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    
    if len(kata1) != len(kata2):
        return False
    
    return sorted(kata1) == sorted(kata2)

print("Masukkan dua kata untuk dicek apakah mereka anagram")

# Inputan
kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

# Panggil fungsi untuk di cek
hasil = cek_anagram(kata_pertama, kata_kedua)

# hasil
print(f"\nHasil Pengecekan:")
print(f"Kata 1: '{kata_pertama}'")
print(f"Kata 2: '{kata_kedua}'")

if hasil:
    print(" Kedua kata merupakan ANAGRAM")
else:
    print(" Kedua kata BUKAN anagram")

print(f"Nilai yang dikembalikan: {hasil}")