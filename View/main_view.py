from Controller import auth_controller
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuUtama():
    while True:
        clear()
        print("+=================================+")
        print("|     Selamat Datang Di Program   |")
        print("|   Pelayanan Konsultasi Terkait  |")
        print("|   Energi Bersih yang Tersedia   |")
        print("+=================================+")
        print("| [1]. Login                      |")
        print("| [2]. Daftar                     |")
        print("| [3]. Keluar                     |")
        print("+=================================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
            if pilihan == 1:
                auth_controller.login()
            elif pilihan == 2:
                auth_controller.daftar()
            elif pilihan == 3:
                clear()
                print("+============================================+")
                print("| Terima Kasih Telah Menggunakan Program Ini |")
                print("+============================================+")
                break
            else:
                clear()
                print("+===============================+")
                print("| Masukkan Tidak Ada Di Pilihan |")
                print("+===============================+")
                input("Tekan enter untuk melanjutkan...")
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            try:
                input("Tekan enter untuk melanjutkan...")
            except:
                print("Mohon Perhatikan Masukan")
