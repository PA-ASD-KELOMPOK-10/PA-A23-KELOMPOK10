import os
from Controller import anggota_controller as anggota

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuAnggota(nama):
    while True:
        clear()
        print("+========================+")
        print("| Selamat Datang Anggota |")
        print("+========================+")
        print("| [1]. Tampilkan Tugas   |")
        print("| [2]. Konfirmasi Tugas  |")
        print("| [3]. Keluar            |")
        print("+========================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
            if pilihan == 1:
                anggota.menuAnggotaTampilkanTugas(nama)
            elif pilihan == 2:
                anggota.menuAnggotaKonfirmasiTugas(nama)
            elif pilihan == 3:
                break
            else:
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
                input("Tekan enter untuk melanjutkan...")
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")