n = int(input("Masukkan tinggi piramida (n): "))

for i in range(1, n + 1):

    for j in range(1, n - i + 2):
        print(j, end=" ")

    for spasi in range(1, (i - 1) * 2 + 1):
        print("  ", end="") 

    for j in range(n - i + 1, 0, -1):
        print(j, end=" ")
    print()