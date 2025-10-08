lama_parkir = int(input("silahkan masukkan lama parkir anda (jam) :"))
vip = input("apakah anda member vip? ya/tidak :")

# # penyeleksian
if vip == "ya":
    biaya = 0
else:
    if lama_parkir <= 24:  
        if lama_parkir <= 2:
            biaya = 5000
        else:
            biaya = 5000 + (lama_parkir - 2) * 3000
            if biaya > 20000:
                biaya = 20000
    else: 
        hari_penuh = lama_parkir // 24     
        sisa_jam = lama_parkir % 24       
        biaya = hari_penuh * 20000  

        if sisa_jam == 0:
            pass 
        elif sisa_jam <= 12:
             biaya = sisa_jam  * 3000 + 20000
        else:
            biaya = sisa_jam  * 3000 + 20000 

# HASIL
print(f"total biaya parkir anda sebesar: Rp{biaya}")