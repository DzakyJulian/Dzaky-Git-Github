# Dzaky Julian Putranto 2400790
# RPL 1-C

nilai = input("Masukkan nilai (pisahkan nilai selanjutnya dengan koma): ") #string

def rerata_nilai(nilai):
    nilai = [float(i) for i in nilai.split(',')] # konversi input (str) ke float &
    # membedakan nilai inputan selanjutnya dari nilai inputan sebelumnya

    total_inp = len(nilai) # untuk mendapatkan angka pembagi
    total = sum(nilai) # untuk mendapatkan total nilai dari seluruh inputan
    rerataNilai = total / total_inp # rumus rata-rata nilai
    return rerataNilai

print("Rata-rata nilai = ",rerata_nilai(nilai))