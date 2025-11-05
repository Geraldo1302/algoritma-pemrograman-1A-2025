def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
n = int(input("masukkan bilangan bulat non - negatif: "))

if n < 0:
    print("maaf, bilangan harus non negatif")
else:
    hasil = faktorial(n)
    print(f"hasil dari {n}! adalah {faktorial(n)}")

