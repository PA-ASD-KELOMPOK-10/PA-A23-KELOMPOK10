from Controller import admin_controller as admin
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuAdmin():
    while True:
        clear()
        print("+======================+")
        print("| Selamat Datang Admin |")
        print("+======================+")
        print("| [1]. Laporan         |")
        print("| [2]. Tugas           |")
        print("| [3]. Keluar          |")
        print("+======================+")
        pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
        if pilihan == 1:
            menuAdminLaporan()
        elif pilihan == 2:
            menuAdminTugas()
        elif pilihan == 3:
            break
        else:
            print("+==============================+")
            print("| Inputan Tidak Ada Di Pilihan |")
            print("+==============================+")
            input("Tekan enter untuk melanjutkan...")

def menuAdminLaporan():
    while True:
        clear()
        admin.ambilDataLaporan()
        print("+========================+")
        print("|         Laporan        |")
        print("+========================+")
        print("| [1]. Buat Laporan      |")
        print("| [2]. Tampilkan Laporan |")
        print("| [3]. Perbarui Laporan  |")
        print("| [4]. Hapus Laporan     |")
        print("| [5]. Cari Laporan      |")
        print("| [6]. Urutkan Laporan   |")
        print("| [7]. Keluar            |")
        print("+========================+")
        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            admin.menuBuatLaporan()
        elif pilihan == 2:
            admin.menuTampilkanLaporan()
        elif pilihan == 3:
            admin.menuPerbaruiLaporan()
        elif pilihan == 4:
            admin.menuHapusLaporan()
        elif pilihan == 5:
            admin.menuCariLaporan()
        elif pilihan == 6:
            admin.menuUrutkanLaporan()
        elif pilihan == 7:
            break
        else:
            print("+==============================+")
            print("| Inputan Tidak Ada Di Pilihan |")
            print("+==============================+")
            input("Tekan enter untuk melanjutkan...")

def menuAdminTugas():
    while True:
        clear()
        admin.ambilDataTugas()
        print("+======================+")
        print("|         Tugas        |")
        print("+======================+")
        print("| [1]. Buat Tugas      |")
        print("| [2]. Tampilkan Tugas |")
        print("| [3]. Perbarui Tugas  |")
        print("| [4]. Hapus Tugas     |")
        print("| [5]. Cari Tugas      |")
        print("| [6]. Urutkan Tugas   |")
        print("| [7]. Keluar          |")
        print("+======================+")
        pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6/7]: "))
        if pilihan == 1:
            admin.menuBuatTugas()
        elif pilihan == 2:
            admin.menuTampilkanTugas()
        elif pilihan == 3:
            admin.menuPerbaruiTugas()
        elif pilihan == 4:
            admin.menuHapusTugas()
        elif pilihan == 5:
            admin.menuCariTugas()
        elif pilihan == 6:
            admin.menuUrutkanTugas()
        elif pilihan == 7:
            break
        else:
            print("+==============================+")
            print("| Inputan Tidak Ada Di Pilihan |")
            print("+==============================+")
            input("Tekan enter untuk melanjutkan...")