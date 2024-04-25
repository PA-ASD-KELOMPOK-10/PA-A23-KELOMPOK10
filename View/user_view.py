from Controller import user_controller as user
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuUser(nama):
    while True:
        clear()
        pesan = f"| Selamat Datang {nama} |"
        print("+" + "=" * (len(pesan) - 2) + "+")
        print(pesan)
        print("+" + "=" * (len(pesan) - 2) + "+")
        print("| [1]. Buat Laporan" + " " * (len(pesan) - 20)  + "|")
        print("| [2]. Cek Laporan " + " " * (len(pesan) - 20)  + "|" )
        print("| [3]. Keluar      " + " " * (len(pesan) - 20)  + "|" )
        print("+" + "=" * (len(pesan) - 2) + "+")
        try:
            pilihan = int(input("Masukkan Pilihan: "))
            if pilihan == 1:
                user.menuBuatLaporan(nama)
            elif pilihan == 2:
                user.menuCekLaporan(nama)
            elif pilihan == 3:
                break
            else:
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
                input("Tekan enter untuk melanjutkan...")
        except Exception as e:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")