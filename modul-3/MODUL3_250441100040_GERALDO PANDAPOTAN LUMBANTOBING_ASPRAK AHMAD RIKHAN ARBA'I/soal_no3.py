kalimat = input("Masukkan sebuah kalimat: ")
vokal = "aiueoAIUEO"  

jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
huruf_vokal = ""  
huruf_konsonan = ""  

for huruf in kalimat: 
    if huruf in vokal:
        jumlah_vokal += 1
        huruf_vokal = huruf_vokal + huruf + " "
    elif huruf != " ":
        jumlah_konsonan += 1
        huruf_konsonan = huruf_konsonan + huruf + " "

if kalimat != "":
    jumlah_kata = 1
    for huruf in kalimat:
        if huruf == " ":
            jumlah_kata += 1

# Menampilkan hasil 
print("\nHasil Analisis Kalimat")
print("----------------------------")
print("Jumlah huruf vokal    :", jumlah_vokal)
print("Jumlah huruf konsonan :", jumlah_konsonan)
print("Jumlah kata           :", jumlah_kata)
print("Huruf vokal yang muncul   :", huruf_vokal)
print("Huruf konsonan yang muncul:", huruf_konsonan)
