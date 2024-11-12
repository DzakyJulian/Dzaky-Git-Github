# Dzaky Julian Putranto 2400790
# RPL 1-C

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    hasil = [0, 1]  # 2 angka pertama sebagai syarat fibonacci
    for i in range(2, n):  # mulai dari indeks ke 2, karna indeks ke 0 & ke 1 adalah 0 dan 1
        hasil.append(hasil[-1] + hasil[-2])  # mengambil 2 angka terakhir dari deret untuk dijumlahkan
        # penjumlahan akan terus mengulang sampai parameter n
    return hasil

n = int(input("Masukkan jumlah (n): "))
print(fibonacci(n))

