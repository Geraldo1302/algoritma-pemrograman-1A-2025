def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    if len(kata1) != len(kata2):
        return False

    return sorted(kata1) == sorted(kata2)

print(" PENGECEKAN ANAGRAM ")
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata1, kata2)

print(f"Kata 1: {kata1}")
print(f"Kata 2: {kata2}")

if hasil:
    print("KEDUA KATA MERUPAKAN ANAGRAM")
else:
    print("KEDUA KATA BUKAN ANAGRAM")

print(f"Nilai yang dikembalikan: {hasil}")