# Dzaky Julian Putranto 2400790
# RPL 1-C

print("Waktu mulai:")
jamMulai = int(input("Jam: "))
menitMulai = int(input("Menit: "))
detikMulai = int(input("Detik: "))

print("\nWaktu selesai:")
jamSelesai = int(input("Jam: "))
menitSelesai = int(input("Menit: "))
detikSelesai = int(input("Detik: "))

def selisih():
    jam = jamSelesai - jamMulai
    menit = menitSelesai - menitMulai
    detik = detikSelesai - detikMulai

    
    if detik < 0: # agar tidak ada angka mines
        detik += 60
        menit -= 1
    
    if menit < 0: # agar tidak ada angka mines
        menit += 60
        jam -= 1

    if jamSelesai < jamMulai: #agar bisa menghitung sampai hitungan hari
        jam += 24

    return jam,menit,detik
 

jam, menit, detik = selisih()
print("Hitung selisih: ")
print(f"{jam} Jam - {menit} Menit - {detik} Detik")

#Tes tes tes 