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
        print("| [3]. Anggota         |")
        print("| [4]. User            |")
        print("| [5]. Keluar          |")
        print("+======================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5]: "))
            if pilihan == 1:
                menuAdminLaporan()
            elif pilihan == 2:
                menuAdminTugas()
            elif pilihan == 3:
                menuAdminAnggota()
            elif pilihan == 4:
                menuAdminUser()
            elif pilihan == 5:
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
            try:
                input("Tekan enter untuk melanjutkan...")
            except:
                print("Mohon Perhatikan Masukan")


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
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6/7]: "))
            if pilihan == 1:
                admin.menuBuatLaporan()
            elif pilihan == 2:
                menuTampilkanLaporan()
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
                clear()
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
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
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6/7]: "))
            if pilihan == 1:
                admin.menuBuatTugas()
            elif pilihan == 2:
                menuTampilkanTugas()
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
                clear()
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
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


def menuAdminAnggota():
    while True:
        clear()
        admin.ambilDataAnggota()
        print("+========================+")
        print("|         Anggota        |")
        print("+========================+")
        print("| [1]. Buat Anggota      |")
        print("| [2]. Tampilkan Anggota |")
        print("| [3]. Perbarui Anggota  |")
        print("| [4]. Hapus Anggota     |")
        print("| [5]. Cari Anggota      |")
        print("| [6]. Urutkan Anggota   |")
        print("| [7]. Keluar            |")
        print("+=========================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6/7]: "))
            if pilihan == 1:
                admin.menuBuatAnggota()
            elif pilihan == 2:
                admin.menuTampilkanAnggota()
            elif pilihan == 3:
                admin.menuPerbaruiAnggota()
            elif pilihan == 4:
                admin.menuHapusAnggota()
            elif pilihan == 5:
                admin.menuCariAnggota()
            elif pilihan == 6:
                admin.menuUrutkanAnggota()
            elif pilihan == 7:
                break
            else:
                clear()
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
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


def menuAdminUser():
    while True:
        clear()
        admin.ambilDataUser()
        print("+=====================+")
        print("|         User        |")
        print("+=====================+")
        print("| [1]. Buat User      |")
        print("| [2]. Tampilkan User |")
        print("| [3]. Perbarui User  |")
        print("| [4]. Hapus User     |")
        print("| [5]. Cari User      |")
        print("| [6]. Urutkan User   |")
        print("| [7]. Keluar         |")
        print("+=====================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6/7]: "))
            if pilihan == 1:
                admin.menuBuatUser()
            elif pilihan == 2:
                admin.menuTampilkanUser()
            elif pilihan == 3:
                admin.menuPerbaruiUser()
            elif pilihan == 4:
                admin.menuHapusUser()
            elif pilihan == 5:
                admin.menuCariUser()
            elif pilihan == 6:
                admin.menuUrutkanUser()
            elif pilihan == 7:
                break
            else:
                clear()
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
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


def menuTampilkanLaporan():
    while True:
        clear()
        print("+===============================+")
        print("|         Menu Tampilkan        |")
        print("+===============================+")
        print("| [1]. Tampilkan Laporan        |")
        print("| [2]. Tampilkan Isi Laporan    |")
        print("| [3]. Tampilkan Lokasi Laporan |")
        print("| [4]. Tampilkan Respon Admin   |")
        print("| [5]. Keluar                   |")
        print("+===============================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5]: "))
            if pilihan == 1:
                admin.tampilkanLaporan("laporan")
            elif pilihan == 2:
                admin.tampilkanLaporan("isi")
            elif pilihan == 3:
                admin.tampilkanLaporan("lokasi")
            elif pilihan == 4:
                admin.tampilkanLaporan("respon")
            elif pilihan == 5:
                break
            else:
                clear()
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
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


def menuTampilkanTugas():
    while True:
        clear()
        print("+===============================+")
        print("|         Menu Tampilkan        |")
        print("+===============================+")
        print("| [1]. Tampilkan Tugas          |")
        print("| [2]. Tampilkan Tugas Laporan  |")
        print("| [3]. Tampilkan Lokasi Laporan |")
        print("| [4]. Keluar                   |")
        print("+===============================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4]: "))
            if pilihan == 1:
                admin.tampilkanTugas("tugas")
            elif pilihan == 2:
                admin.tampilkanTugas("tugaslaporan")
            elif pilihan == 3:
                admin.tampilkanTugas("lokasi")
            elif pilihan == 4:
                break
            else:
                clear()
                print("+==============================+")
                print("| Inputan Tidak Ada Di Pilihan |")
                print("+==============================+")
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

