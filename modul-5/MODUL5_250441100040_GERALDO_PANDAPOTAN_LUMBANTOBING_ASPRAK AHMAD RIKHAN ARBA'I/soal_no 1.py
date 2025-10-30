def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("masukkan bilangan bulat non - negatiif: "))

if n < 0:
    print("maaf, bilangan harus non negatif")
else:
    hasil = factorial(n)
    print(f"hasil dari {n}! faktorial{n} adalah: 1{hasil}")


    