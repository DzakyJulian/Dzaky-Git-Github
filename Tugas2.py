# Dzaky Julian Putranto 2400790
# RPL 1-C

print("---|HALAMAN LOGIN|---")
username = "Daspro2023"
password = "Latihan"
percobaan = 3 # jumlah batas percobaan

Uname = False # kondisi username kosong
login = False # kondisi awal (belum login)

def auth():
    global Uname, login, percobaan

    if not login:
        while percobaan > 0:
            if not Uname:
                un = input("Masukkan username: ")
                if un == username:
                    Uname = True # ubah menjadi True jika input sesuai agar tidak mengisi ulang username 
                else:
                    percobaan -= 1
                    print(f"Username salah! coba lagi.\nKesempatan Anda tersisa {percobaan} lagi.")
                    print("-"*20)
            
            if Uname is True:
                pw = input("Masukkan password Anda: ")
                if pw == password:
                    login = True
                    print("-"*20)
                    print("Berhasil login")
                    print("-"*20)
                    break
                else:
                    percobaan -= 1
                    print(f"Password salah! coba lagi.\nKesempatan Anda tersisa {percobaan} lagi.")
                    print("-"*20)
        if not login:
            print("ANDA DIBLOKIR! Terlalu banyak percobaan.")
    else:
        print("Anda sudah login.")

auth()
                
        