from Model.database import koneksiDatabase
from Controller import linkedlist_controller as linkedlist
from prettytable import PrettyTable
import mysql.connector
import os
import re
db, cursor = koneksiDatabase()

tugasLinkedList = linkedlist.LinkedList()
laporanLinkedList = linkedlist.LinkedList()
anggotaLinkedList = linkedlist.LinkedList()
userLinkedList = linkedlist.LinkedList()

def clear():
    os.system("cls" if os.name == "nt" else "clear")



# Laporan



def menuBuatLaporan():
    while True:
        clear()
        print("+==============+")
        print("| Buat Laporan |")
        print("+==============+")
        try:
            idUser = int(input("Masukkan ID User: "))
            if cekIDUser(idUser):
                isiLaporan = str(input("Masukkan Isi Laporan: "))
                if len(isiLaporan) <= 500:
                    if isiLaporan.strip():
                        lokasiLaporan = str(input("Masukkan Lokasi Laporan: "))
                        if len(lokasiLaporan) <= 100:
                            if lokasiLaporan.strip():
                                query = "INSERT INTO laporan (ID_User, Isi_Laporan, Lokasi_Laporan) VALUES (%s, %s, %s)"
                                cursor.execute(query, (idUser, isiLaporan, lokasiLaporan))
                                db.commit()
                                clear()
                                print("+=========================+")
                                print("| Laporan Berhasil Dibuat |")
                                print("+=========================+")
                                input("Tekan enter untuk melanjutkan...")
                                break
                            else:
                                clear()
                                print("+===================================+")
                                print("| Lokasi Laporan Tidak Boleh Kosong |")
                                print("+===================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+====================================================+")
                            print("| Lokasi Laporan Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+====================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+================================+")
                        print("| Isi Laporan Tidak Boleh Kosong |")
                        print("+================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+=================================================+")
                    print("| Isi Laporan Tidak Boleh Lebih Dari 500 Karakter |")
                    print("+=================================================+")
                    input("Tekan enter untuk melanjutkan...")

            else:
                clear()
                print("+===============================+")
                print("| ID User Tidak Ada Di Database |")
                print("+===============================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def tampilkanLaporan(laporan):
    clear()
    ambilDataLaporan()
    tabel = PrettyTable()
    if laporan == "laporan":
        tabel.field_names = ["ID Laporan", "ID User", "Isi Laporan", "Lokasi Laporan", "Status Laporan", "Respon Admin"]
        current = laporanLinkedList.head
        while current:
            data = current.data
            isiLaporan = data["Isi_Laporan"]
            lokasiLaporan = data["Lokasi_Laporan"]
            responAdmin = str(data["respon_admin"])
            if len(isiLaporan) > 50:
                isiLaporan = data["Isi_Laporan"][:47] + "..."
            if len(lokasiLaporan) > 50:
                lokasiLaporan = data["Lokasi_Laporan"][:47] + "..."
            if len(responAdmin) > 50:
                responAdmin = str(data["respon_admin"][:47] + "...")
            tabel.add_row([data["ID_Laporan"], data["ID_User"], isiLaporan, lokasiLaporan, data["status_laporan"], responAdmin])
            current = current.next
        clear()
        print(tabel)
        input("Tekan enter untuk melanjutkan...")
    elif laporan == "isi":
        tabel.field_names = ["ID Laporan", "ID User", "Isi Laporan"]
        current = laporanLinkedList.head
        while current:
            data = current.data
            tabel.add_row([data["ID_Laporan"], data["ID_User"], data["Isi_Laporan"]])
            current = current.next
        clear()
        print(tabel)
        input("Tekan enter untuk melanjutkan...")
    elif laporan == "lokasi":
        tabel.field_names = ["ID Laporan", "ID User", "Lokasi Laporan"]
        current = laporanLinkedList.head
        while current:
            data = current.data
            tabel.add_row([data["ID_Laporan"], data["ID_User"], data["Lokasi_Laporan"]])
            current = current.next
        clear()
        print(tabel)
        input("Tekan enter untuk melanjutkan...")
    elif laporan == "respon":
        tabel.field_names = ["ID Laporan", "ID User", "Respon Admin"]
        current = laporanLinkedList.head
        while current:
            data = current.data
            tabel.add_row([data["ID_Laporan"], data["ID_User"], data["respon_admin"]])
            current = current.next
        clear()
        print(tabel)
        input("Tekan enter untuk melanjutkan...")

def menuPerbaruiLaporan():
    while True:
        clear()
        print("+==================================+")
        print("|         Perbarui Laporan         |")
        print("+==================================+")
        print("| [1]. Perbarui ID User Pada Tugas |")
        print("| [2]. Perbarui Isi Laporan        |")
        print("| [3]. Perbarui Lokasi Laporan     |")
        print("| [4]. Perbarui Status Laporan     |")
        print("| [5]. Perbarui Respon Admin       |")
        print("| [6]. Keluar                      |")
        print("+==================================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6]: "))
            if pilihan == 1:
                idLaporan = int(input("Masukkan ID Laporan: "))
                if cekIDLaporan(idLaporan):
                    idUser = int(input("Masukkan ID User Yang Baru: "))
                    if str(idUser).strip():
                        if cekIDUser(idUser):
                            query = "UPDATE laporan SET ID_User = %s WHERE ID_Laporan = %s"
                            cursor.execute(query, (idUser, idLaporan))
                            db.commit()
                            clear()
                            print("+=========================+")
                            print("| ID User Berhasil Diubah |")
                            print("+=========================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+======================================+")
                            print("|  ID User Tidak Ditemukan Di Database |")
                            print("+======================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+=======================+")
                        print("| ID Tidak Boleh Kosong |")
                        print("+=======================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Laporan Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 2:
                idLaporan = int(input("Masukkan ID Laporan: "))
                if cekIDLaporan(idLaporan):
                    isiLaporan = str(input("Masukkan Isi Laporan Yang Baru: "))
                    if isiLaporan.strip():
                        if len(isiLaporan) <= 500:
                            query = "UPDATE laporan SET Isi_Laporan = %s WHERE ID_Laporan = %s"
                            cursor.execute(query, (isiLaporan, idLaporan))
                            db.commit()
                            clear()
                            print("+=============================+")
                            print("| Isi Laporan Berhasil Dibuah |")
                            print("+=============================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+==================================================+")
                            print("|  Isi Laporan Tidak Boleh Lebih Dari 500 Karakter |")
                            print("+==================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+================================+")
                        print("| Isi Laporan Tidak Boleh Kosong |")
                        print("+================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Laporan Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 3:
                idLaporan = int(input("Masukkan ID Laporan: "))
                if cekIDLaporan(idLaporan):
                    lokasiLaporan = str(input("Masukkan Lokasi Laporan Yang Baru: "))
                    if lokasiLaporan.strip():
                        if len(lokasiLaporan) <= 100:
                            query = "UPDATE laporan SET Lokasi_Laporan = %s WHERE ID_Laporan = %s"
                            cursor.execute(query, (lokasiLaporan, idLaporan))
                            db.commit()
                            clear()
                            print("+================================+")
                            print("| Lokasi Laporan Berhasil Dibuah |")
                            print("+================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+=====================================================+")
                            print("|  Lokasi Laporan Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+=====================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+===================================+")
                        print("| Lokasi Laporan Tidak Boleh Kosong |")
                        print("+===================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Laporan Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 4:
                idLaporan = int(input("Masukkan ID Laporan: "))
                if cekIDLaporan(idLaporan):
                    statusLaporan = str(input("Masukkan Status Laporan Yang Baru: "))
                    if statusLaporan.strip():
                        if len(statusLaporan) <= 255:
                            query = "UPDATE laporan SET status_laporan = %s WHERE ID_Laporan = %s"
                            cursor.execute(query, (statusLaporan, idLaporan))
                            db.commit()
                            clear()
                            print("+================================+")
                            print("| Status Laporan Berhasil Dibuah |")
                            print("+================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+=====================================================+")
                            print("|  Status Laporan Tidak Boleh Lebih Dari 255 Karakter |")
                            print("+=====================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+===================================+")
                        print("| Status Laporan Tidak Boleh Kosong |")
                        print("+===================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Laporan Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 5:
                idLaporan = int(input("Masukkan ID Laporan: "))
                if cekIDLaporan(idLaporan):
                    responAdmin = str(input("Masukkan Respon Laporan Yang Baru: "))
                    if responAdmin.strip():
                        if len(responAdmin) <= 255:
                            query = "UPDATE laporan SET respon_admin = %s WHERE ID_Laporan = %s"
                            cursor.execute(query, (responAdmin, idLaporan))
                            db.commit()
                            clear()
                            print("+==============================+")
                            print("| Respon Admin Berhasil Dibuah |")
                            print("+==============================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+===================================================+")
                            print("|  Respon Admin Tidak Boleh Lebih Dari 255 Karakter |")
                            print("+===================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+=================================+")
                        print("| Respon Admin Tidak Boleh Kosong |")
                        print("+=================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+======================================+")
                    print("| ID Admin Tidak Ditemukan Di Database |")
                    print("+======================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 6:
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
            input("Tekan enter untuk melanjutkan...")
def menuHapusLaporan():
    while True:
        clear()
        print("+=================+")
        print("|  Hapus Laporan  |")
        print("+=================+")
        try:
            idLaporan = int(input("Masukkan ID Laporan Yang Ingin Dihapus: "))
            if cekIDLaporan(idLaporan):
                query = "DELETE FROM laporan WHERE ID_Laporan = %s"
                cursor.execute(query, (idLaporan, ))
                db.commit()
                clear()
                print("+==========================+")
                print("| Laporan Berhasil Dihapus |")
                print("+==========================+")
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+========================================+")
                print("| ID Laporan Tidak Ditemukan Di Database |")
                print("+========================================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except mysql.connector.Error as error:
            clear()
            print(f"Error MySQL: {error}")
            input("Tekan enter untuk melanjutkan...")
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuCariLaporan():
    while True:
        clear()
        print("+==============+")
        print("| Cari Laporan |")
        print("+==============+")
        try:
            idLaporan = int(input("Masukkan ID Laporan Yang Ingin Dicari: "))
            node = laporanLinkedList.jumpSearchID(idLaporan, "laporan")
            if node:
                clear()
                print("+===================+")
                print("| Laporan Ditemukan |")
                print("+===================+")
                input("Tekan enter untuk melanjutkan...")
                clear()
                dataLaporan = node.data
                tabel = PrettyTable()
                tabel.field_names = ["ID Laporan", "ID User", "Isi Laporan", "Lokasi Laporan", "Status Laporan", "Respon Admin"]
                tabel.add_row([dataLaporan["ID_Laporan"], dataLaporan["ID_User"], dataLaporan["Isi_Laporan"], dataLaporan["Lokasi_Laporan"], dataLaporan["status_laporan"], dataLaporan["respon_admin"]])
                print(tabel)
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+============================+")
                print("| ID Laporan Tidak Ditemukan |")
                print("+============================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuUrutkanLaporan():
    while True:
        clear()
        print("+=================+")
        print("| Urutkan Laporan |")
        print("+=================+")
        print("| [1]. Ascending  |")
        print("| [2]. Descending |")
        print("| [3]. Keluar     |")
        print("+=================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
            if pilihan == 1:
                urutkanLaporan("Ascending")
            elif pilihan == 2:
                urutkanLaporan("Descending")
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

def urutkanLaporan(urut):
    clear()
    ambilDataLaporan()
    daftarID = []
    current = laporanLinkedList.head
    while current:
        daftarID.append(current.data["ID_Laporan"])
        current = current.next
    if urut == "Ascending":
        daftarIDTerurut = laporanLinkedList.quickSort(daftarID)
    elif urut == "Descending":
        daftarIDTerurut = laporanLinkedList.quickSortDescending(daftarID)

    tabel = PrettyTable()
    tabel.field_names = ["ID Laporan", "ID User", "Isi Laporan", "Lokasi Laporan", "Status Laporan", "Respon Admin"]

    for idLaporan in daftarIDTerurut:
        node = laporanLinkedList.jumpSearchID(idLaporan, "laporan")
        if node:
            data = node.data
            isiLaporan = data["Isi_Laporan"]
            lokasiLaporan = data["Lokasi_Laporan"]
            responAdmin = str(data["respon_admin"])
            if len(isiLaporan) > 50:
                isiLaporan = data["Isi_Laporan"][:47] + "..."
            if len(lokasiLaporan) > 50:
                lokasiLaporan = data["Lokasi_Laporan"][:47] + "..."
            if len(responAdmin) > 50:
                responAdmin = str(data["respon_admin"][:47] + "...")
            tabel.add_row([data["ID_Laporan"], data["ID_User"], isiLaporan, lokasiLaporan, data["status_laporan"], responAdmin])
    
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")



# Tugas



def menuBuatTugas():
    while True:
        clear()
        print("+==============+")
        print("|  Buat Tugas  |")
        print("+==============+")
        try:
            idAdmin = int(input("Masukkan ID Admin: "))
            if cekIDAdmin(idAdmin):
                idAnggota = int(input("Masukkan ID Anggota: "))
                if cekIDAnggota(idAnggota):
                    tugasLaporan = str(input("Masukkan Tugas Laporan: "))
                    if len(tugasLaporan) <= 100:
                        if tugasLaporan.strip():
                            lokasiLaporan = str(input("Masukkan Lokasi Laporan: "))
                            if len(lokasiLaporan) <= 100:
                                if lokasiLaporan.strip():
                                    query = "INSERT INTO tugas (ID_Admin, ID_Anggota, Tugas_Laporan, Lokasi_Laporan) VALUES (%s, %s, %s, %s)"
                                    cursor.execute(query, (idAdmin, idAnggota, tugasLaporan, lokasiLaporan))
                                    db.commit()
                                    clear()
                                    print("+=======================+")
                                    print("| Tugas Berhasil Dibuat |")
                                    print("+=======================+")
                                    input("Tekan enter untuk melanjutkan...")
                                    break
                                else:
                                    clear()
                                    print("+===================================+")
                                    print("| Lokasi Laporan Tidak Boleh Kosong |")
                                    print("+===================================+")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+====================================================+")
                                print("| Lokasi Laporan Tidak Boleh Lebih Dari 100 Karakter |")
                                print("+====================================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+==================================+")
                            print("| Tugas Laporan Tidak Boleh Kosong |")
                            print("+==================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+===================================================+")
                        print("| Tugas Laporan Tidak Boleh Lebih Dari 100 Karakter |")
                        print("+===================================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+==================================+")
                    print("| ID Anggota Tidak Ada Di Database |")
                    print("+==================================+")
                    input("Tekan enter untuk melanjutkan...")
            else:
                clear()
                print("+================================+")
                print("| ID Admin Tidak Ada Di Database |")
                print("+================================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def tampilkanTugas(tugas):
    clear()
    ambilDataTugas()
    tabel = PrettyTable()
    if tugas == "tugas":
        tabel.field_names = ["ID Tugas", "ID Admin", "ID Anggota", "Tugas Laporan", "Lokasi Laporan", "Status Tugas"]
        current = tugasLinkedList.head
        while current:
            data = current.data
            tugasLaporan = data["Tugas_Laporan"]
            lokasiLaporan = data["Lokasi_Laporan"]
            if len(tugasLaporan) > 50:
                tugasLaporan = data["Tugas_Laporan"][:47] + "..."
            if len(lokasiLaporan) > 50:
                lokasiLaporan = data["Lokasi_Laporan"][:47] + "..."
            tabel.add_row([data["ID_Tugas"], data["ID_Admin"], data["ID_Anggota"], tugasLaporan, lokasiLaporan, data["status_tugas"]])
            current = current.next
        clear()
        print(tabel)
        input("Tekan enter untuk melanjutkan...")
    elif tugas == "tugaslaporan":
        tabel.field_names = ["ID Tugas", "Tugas Laporan"]
        current = tugasLinkedList.head
        while current:
            data = current.data
            tabel.add_row([data["ID_Tugas"], data["Tugas_Laporan"]])
            current = current.next
        clear()
        print(tabel)
        input("Tekan enter untuk melanjutkan...")
    elif tugas == "lokasi":
        tabel.field_names = ["ID Tugas", "Lokasi Laporan"]
        current = tugasLinkedList.head
        while current:
            data = current.data
            tabel.add_row([data["ID_Tugas"], data["Lokasi_Laporan"]])
            current = current.next
        clear()
        print(tabel)
        input("Tekan enter untuk melanjutkan...")

def menuPerbaruiTugas():
    while True:
        clear()
        print("+=====================================+")
        print("|            Perbarui Tugas           |")
        print("+=====================================+")
        print("| [1]. Perbarui ID Admin Pada Tugas   |")
        print("| [2]. Perbarui ID Anggota Pada Tugas |")
        print("| [3]. Perbarui Tugas Laporan         |")
        print("| [4]. Perbarui Lokasi Laporan        |")
        print("| [5]. Perbarui Status Laporan        |")
        print("| [6]. Keluar                         |")
        print("+=====================================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6]: "))
            if pilihan == 1:
                idTugas = int(input("Masukkan ID Tugas: "))
                if cekIDTugas(idTugas):
                    idAdmin = int(input("Masukkan ID Admin Yang Baru: "))
                    if str(idAdmin).strip():
                        if len(str(idAdmin)) <= 11:
                            if cekIDAdmin(idAdmin):
                                query = "UPDATE tugas SET ID_Admin = %s WHERE ID_Tugas = %s"
                                cursor.execute(query, (idAdmin, idTugas))
                                db.commit()
                                clear()
                                print("+==========================+")
                                print("| ID Admin Berhasil Diubah |")
                                print("+==========================+")
                                input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+======================================+")
                                print("| ID Admin Tidak Ditemukan Di Database |")
                                print("+======================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+=============================================+")
                            print("| ID Admin Tidak Boleh Lebih Dari 11 Karakter |")
                            print("+=============================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        print("+=============================+")
                        print("| ID Admin Tidak Boleh Kosong |")
                        print("+=============================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+======================================+")
                    print("| ID Tugas Tidak Ditemukan Di Database |")
                    print("+======================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 2:
                idTugas = int(input("Masukkan ID Tugas: "))
                if cekIDTugas(idTugas):
                    idAnggota = int(input("Masukkan ID Anggota Yang Baru: "))
                    if str(idAnggota).strip():
                        if len(str(idAnggota)) <= 11:
                            if cekIDAnggota(idAnggota):
                                query = "UPDATE tugas SET ID_Anggota = %s WHERE ID_Tugas = %s"
                                cursor.execute(query, (idAnggota, idTugas))
                                db.commit()
                                clear()
                                print("+============================+")
                                print("| ID Anggota Berhasil Diubah |")
                                print("+============================+")
                                input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+======================================+")
                                print("| ID Anggota Tidak Ditemukan Di Database |")
                                print("+======================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+=============================================+")
                            print("| ID Anggota Tidak Boleh Lebih Dari 11 Karakter |")
                            print("+=============================================+")
                            input("Tekan enter untuk melanjutkan...")

                    else:
                        print("+=============================+")
                        print("| ID Anggota Tidak Boleh Kosong |")
                        print("+=============================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+======================================+")
                    print("| ID Tugas Tidak Ditemukan Di Database |")
                    print("+======================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 3:
                idTugas = int(input("Masukkan ID Tugas: "))
                if cekIDTugas(idTugas):
                    tugasLaporan = str(input("Masukkan Tugas Laporan Yang Baru: "))
                    if tugasLaporan.strip():
                        if len(tugasLaporan) <= 100:
                            query = "UPDATE tugas SET Tugas_Laporan = %s WHERE ID_Tugas = %s"
                            cursor.execute(query, (tugasLaporan, idTugas))
                            db.commit()
                            clear()
                            print("+===============================+")
                            print("| Tugas Laporan Berhasil Diubah |")
                            print("+===============================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+===================================================+")
                            print("| Tugas Laporan Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+===================================================+")
                    else:
                        print("+==================================+")
                        print("| Tugas Laporan Tidak Boleh Kosong |")
                        print("+==================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+======================================+")
                    print("| ID Tugas Tidak Ditemukan Di Database |")
                    print("+======================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 4:
                idTugas = int(input("Masukkan ID Tugas: "))
                if cekIDTugas(idTugas):
                    lokasiLaporan = str(input("Masukkan Lokasi Laporan Yang Baru: "))
                    if lokasiLaporan.strip():
                        if len(lokasiLaporan) <= 100:
                            query = "UPDATE tugas SET Lokasi_Laporan = %s WHERE ID_Tugas = %s"
                            cursor.execute(query, (lokasiLaporan, idTugas))
                            db.commit()
                            clear()
                            print("+================================+")
                            print("| Lokasi Laporan Berhasil Diubah |")
                            print("+================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+====================================================+")
                            print("| Lokasi Laporan Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+====================================================+")
                    else:
                        print("+===================================+")
                        print("| Lokasi Laporan Tidak Boleh Kosong |")
                        print("+===================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+======================================+")
                    print("| ID Tugas Tidak Ditemukan Di Database |")
                    print("+======================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 5:
                idTugas = int(input("Masukkan ID Tugas: "))
                if cekIDTugas(idTugas):
                    statusTugas = str(input("Masukkan Status Tugas Yang Baru: "))
                    if statusTugas.strip():
                        if len(statusTugas) <= 100:
                            query = "UPDATE tugas SET status_tugas = %s WHERE ID_Tugas = %s"
                            cursor.execute(query, (statusTugas, idTugas))
                            db.commit()
                            clear()
                            print("+==============================+")
                            print("| Status Tugas Berhasil Diubah |")
                            print("+==============================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+==================================================+")
                            print("| Status Tugas Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+==================================================+")
                    else:
                        print("+=================================+")
                        print("| Status Tugas Tidak Boleh Kosong |")
                        print("+=================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+======================================+")
                    print("| ID Tugas Tidak Ditemukan Di Database |")
                    print("+======================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 6:
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

def menuHapusTugas():
    while True:
        clear()
        print("+===============+")
        print("|  Hapus Tugas  |")
        print("+===============+")
        try:
            idTugas = int(input("Masukkan ID Tugas Yang Ingin Dihapus: "))
            if cekIDTugas(idTugas):
                query = "DELETE FROM tugas WHERE ID_Tugas = %s"
                cursor.execute(query, (idTugas, ))
                db.commit()
                clear()
                print("+========================+")
                print("| Tugas Berhasil Dihapus |")
                print("+========================+")
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+======================================+")
                print("| ID Tugas Tidak Ditemukan Di Database |")
                print("+======================================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except mysql.connector.Error as error:
            clear()
            print(f"Error MySQL: {error}")
            input("Tekan enter untuk melanjutkan...")
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuCariTugas():
    while True:
        clear()
        print("+============+")
        print("| Cari Tugas |")
        print("+============+")
        try:
            idTugas = int(input("Masukkan ID Tugas Yang Ingin Dicari: "))
            node = tugasLinkedList.jumpSearchID(idTugas, "tugas")
            if node:
                clear()
                print("+=================+")
                print("| Tugas Ditemukan |")
                print("+=================+")
                input("Tekan enter untuk melanjutkan...")
                clear()
                dataTugas = node.data
                tabel = PrettyTable()
                tabel.field_names = ["ID Tugas", "ID Admin", "ID Anggota", "Tugas Laporan", "Lokasi Laporan", "Status Laporan"]
                tabel.add_row([dataTugas["ID_Tugas"], dataTugas["ID_Admin"], dataTugas["ID_Anggota"], dataTugas["Tugas_Laporan"], dataTugas["Lokasi_Laporan"], dataTugas["status_tugas"]])
                print(tabel)
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+==========================+")
                print("| ID Tugas Tidak Ditemukan |")
                print("+==========================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuUrutkanTugas():
    while True:
        clear()
        print("+=================+")
        print("|  Urutkan Tugas  |")
        print("+=================+")
        print("| [1]. Ascending  |")
        print("| [2]. Descending |")
        print("| [3]. Keluar     |")
        print("+=================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
            if pilihan == 1:
                urutkanTugas("Ascending")
            elif pilihan == 2:
                urutkanTugas("Descending")
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

def urutkanTugas(urut):
    clear()
    ambilDataTugas()
    daftarID = []
    current = tugasLinkedList.head
    while current:
        daftarID.append(current.data["ID_Tugas"])
        current = current.next

    if urut == "Ascending":
        daftarIDTerurut = tugasLinkedList.quickSort(daftarID)
    elif urut == "Descending":
        daftarIDTerurut = tugasLinkedList.quickSortDescending(daftarID)
    tabel = PrettyTable()
    tabel.field_names = ["ID Tugas", "ID Admin", "ID Anggota", "Tugas Laporan", "Lokasi Laporan", "Status Tugas"]

    for idTugas in daftarIDTerurut:
        node = tugasLinkedList.jumpSearchID(idTugas, "tugas")
        if node:
            data = node.data
            tugasLaporan = data["Tugas_Laporan"]
            lokasiLaporan = data["Lokasi_Laporan"]
            if len(tugasLaporan) > 50:
                tugasLaporan = data["Tugas_Laporan"][:47] + "..."
            if len(lokasiLaporan) > 50:
                lokasiLaporan = data["Lokasi_Laporan"][:47] + "..."
            tabel.add_row([data["ID_Tugas"], data["ID_Admin"], data["ID_Anggota"], tugasLaporan, lokasiLaporan, data["status_tugas"]])

    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")


# Anggota

def menuBuatAnggota():
    while True:
        clear()
        print("+==============+")
        print("| Buat Anggota |")
        print("+==============+")
        try:
            emailAnggota = str(input("Masukkan Email Anggota: "))
            if emailAnggota.strip():
                if cekFormatEmail(emailAnggota):
                    if not cekEmailAnggota(emailAnggota) and not cekEmailAdmin(emailAnggota) and not cekEmailUser(emailAnggota):
                        if len(emailAnggota) <= 100:
                            passwordAnggota = str(input("Masukkan Password Anggota: "))
                            if passwordAnggota.strip():
                                if len(passwordAnggota) <= 255:
                                    namaAnggota = str(input("Masukkan Nama Anggota: "))
                                    if namaAnggota.strip():
                                        if len(namaAnggota) <= 100:
                                            rankingAnggota = int(input("Masukkan Ranking Anggota: "))
                                            if str(rankingAnggota).strip():
                                                if len(str(rankingAnggota)) <= 11:
                                                    keahlianAnggota = str(input("Masukkan Keahlian Anggota: "))
                                                    if keahlianAnggota.strip():
                                                        if len(keahlianAnggota) <= 100:
                                                            query = "INSERT INTO anggota (Nama_Anggota, Rangking_Anggota, Keahlian_Anggota, password_anggota, email_anggota) VALUES (%s, %s, %s, %s, %s)"
                                                            cursor.execute(query, (namaAnggota, rankingAnggota, keahlianAnggota, passwordAnggota, emailAnggota))
                                                            db.commit()
                                                            clear()
                                                            print("+==============================+")
                                                            print("| Akun Anggota Berhasil Dibuat |")
                                                            print("+==============================+")
                                                            input("Tekan enter untuk melanjutkan...")
                                                            break
                                                        else:
                                                            clear()
                                                            print("+======================================================+")
                                                            print("| Keahlian Anggota Tidak Boleh Lebih Dari 100 Karakter |")
                                                            print("+======================================================+")
                                                            input("Tekan enter untuk melanjutkan...")
                                                    else:
                                                        clear()
                                                        print("+=====================================+")
                                                        print("| Keahlian Anggota Tidak Boleh Kosong |")
                                                        print("+=====================================+")
                                                        input("Tekan enter untuk melanjutkan...")
                                                else:
                                                    clear()
                                                    print("+====================================================+")
                                                    print("| Ranking Anggota Tidak Boleh Lebih Dari 11 Karakter |")
                                                    print("+====================================================+")
                                                    input("Tekan enter untuk melanjutkan...")
                                            else:
                                                clear()
                                                print("+====================================+")
                                                print("| Ranking Anggota Tidak Boleh Kosong |")
                                                print("+====================================+")
                                                input("Tekan enter untuk melanjutkan...")
                                        else:
                                            clear()
                                            print("+==================================================+")
                                            print("| Nama Anggota Tidak Boleh Lebih Dari 100 Karakter |")
                                            print("+==================================================+")
                                            input("Tekan enter untuk melanjutkan...")
                                    else:
                                        clear()
                                        print("+=================================+")
                                        print("| Nama Anggota Tidak Boleh Kosong |")
                                        print("+=================================+")
                                        input("Tekan enter untuk melanjutkan...")
                                else:
                                    clear()
                                    print("+======================================================+")
                                    print("| Password Anggota Tidak Boleh Lebih Dari 100 Karakter |")
                                    print("+======================================================+")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+=====================================+")
                                print("| Password Anggota Tidak Boleh Kosong |")
                                print("+=====================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+===================================================+")
                            print("| Email Anggota Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+===================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+===========================================+")
                        print("| Email Anggota Sudah Terdaftar Di Database |")
                        print("+===========================================+")
                        input("Tekan enter untuk melanjutkan...")
                        break
                else:
                    clear()
                    print("+==================================+")
                    print("| Format Email Tidak Sesuai Format |")
                    print("+==================================+")
                    input("Tekan enter untuk melanjutkan...")
                    break
            else:
                clear()
                print("+==================================+")
                print("| Email Anggota Tidak Boleh Kosong |")
                print("+==================================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuTampilkanAnggota():
    clear()
    ambilDataAnggota()
    tabel = PrettyTable()
    tabel.field_names = ["ID Anggota", "Ranking Anggota", "Nama Anggota", "Keahlian Anggota", "Email Anggota", "Password Anggota"]
    current = anggotaLinkedList.head
    while current:
        data = current.data
        tabel.add_row([data["ID_Anggota"], data["Rangking_Anggota"], data["Nama_Anggota"], data["Keahlian_Anggota"], data["email_anggota"], data["password_anggota"]])
        current = current.next
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

def menuPerbaruiAnggota():
    while True:
        clear()
        print("+================================+")
        print("|        Perbarui Anggota        |")
        print("+================================+")
        print("| [1]. Perbarui Email Anggota    |")
        print("| [2]. Perbarui Password Anggota |")
        print("| [3]. Perbarui Nama Anggota     |")
        print("| [4]. Perbarui Keahlian Anggota |")
        print("| [5]. Perbarui Ranking Anggota  |")
        print("| [6]. Keluar                    |")
        print("+================================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6]: "))
            if pilihan == 1:
                idAnggota = int(input("Masukkan ID Anggota: "))
                if cekIDAnggota(idAnggota):
                    emailAnggota = str(input("Masukkan Email Anggota Yang Baru: "))
                    if emailAnggota.strip():
                        if cekFormatEmail(emailAnggota):
                            if not cekEmailAnggota(emailAnggota) and not cekEmailAdmin(emailAnggota) and not cekEmailUser(emailAnggota):
                                if len(emailAnggota) <= 100:
                                    query = "UPDATE anggota SET email_anggota = %s WHERE ID_Anggota = %s"
                                    cursor.execute(query, (emailAnggota, idAnggota))
                                    db.commit()
                                    clear()
                                    print("+===============================+")
                                    print("| Email Anggota Berhasil Diubah |")
                                    print("+===============================+")
                                    input("Tekan enter untuk melanjutkan...")      
                                else:
                                    clear()
                                    print("+===================================================+")
                                    print("| Email Anggota Tidak Boleh Lebih Dari 100 Karakter |")
                                    print("+===================================================+")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+===========================================+")
                                print("| Email Anggota Sudah Terdaftar Di Database |")
                                print("+===========================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+==================================+")
                            print("| Format Email Tidak Sesuai Format |")
                            print("+==================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+==================================+")
                        print("| Email Anggota Tidak Boleh Kosong |")
                        print("+==================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Anggota Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 2:
                idAnggota = int(input("Masukkan ID Anggota: "))
                if cekIDAnggota(idAnggota):
                    passwordAnggota = str(input("Masukkan Password Anggota Yang Baru: "))
                    if passwordAnggota.strip():
                        if len(passwordAnggota) <= 255:
                            query = "UPDATE anggota SET password_anggota = %s WHERE ID_Anggota = %s"
                            cursor.execute(query, (passwordAnggota, idAnggota))
                            db.commit()
                            clear()
                            print("+======================================+")
                            print("| Password Anggota Berhasil Diperbarui |")
                            print("+======================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+======================================================+")
                            print("| Password Anggota Tidak Boleh Lebih Dari 255 Karakter |")
                            print("+======================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+=====================================+")
                        print("| Password Anggota Tidak Boleh Kosong |")
                        print("+=====================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Anggota Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 3:
                idAnggota = int(input("Masukkan ID Anggota: "))
                if cekIDAnggota(idAnggota):
                    namaAnggota = str(input("Masukkan Nama Anggota Yang Baru: "))
                    if namaAnggota.strip():
                        if len(namaAnggota) <= 100:
                            query = "UPDATE anggota SET Nama_Anggota = %s WHERE ID_Anggota = %s"
                            cursor.execute(query, (namaAnggota, idAnggota))
                            db.commit()
                            clear()
                            print("+==================================+")
                            print('| Nama Anggota Berhasil Diperbarui |')
                            print("+==================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+==================================================+")
                            print("| Nama Anggota Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+==================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+=================================+")
                        print("| Nama Anggota Tidak Boleh Kosong |")
                        print("+=================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Anggota Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 4:
                idAnggota = int(input("Masukkan ID Anggota: "))
                if cekIDAnggota(idAnggota):
                    keahlianAnggota = str(input("Masukkan Keahlian Anggota Yang Baru: "))
                    if keahlianAnggota.strip():
                        if len(keahlianAnggota) <= 100:
                            query = "UPDATE anggota SET Keahlian_Anggota = %s WHERE ID_Anggota = %s"
                            cursor.execute(query, (keahlianAnggota, idAnggota))
                            db.commit()
                            clear()
                            print("+======================================+")
                            print('| Keahlian Anggota Berhasil Diperbarui |')
                            print("+======================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+======================================================+")
                            print("| Keahlian Anggota Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+======================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+=====================================+")
                        print("| Keahlian Anggota Tidak Boleh Kosong |")
                        print("+=====================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Anggota Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 5:
                idAnggota = int(input("Masukkan ID Anggota: "))
                if cekIDAnggota(idAnggota):
                    rankingAnggota = int(input("Masukkan Ranking Anggota Yang Baru: "))
                    if str(rankingAnggota).strip():
                        if len(str(rankingAnggota)) <= 11:
                            query = "UPDATE anggota SET Rangking_Anggota = %s WHERE ID_Anggota = %s"
                            cursor.execute(query, (rankingAnggota, idAnggota))
                            db.commit()
                            clear()
                            print("+=====================================+")
                            print('| Ranking Anggota Berhasil Diperbarui |')
                            print("+=====================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+====================================================+")
                            print("| Ranking Anggota Tidak Boleh Lebih Dari 11 Karakter |")
                            print("+====================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+====================================+")
                        print("| Ranking Anggota Tidak Boleh Kosong |")
                        print("+====================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+========================================+")
                    print("| ID Anggota Tidak Ditemukan Di Database |")
                    print("+========================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 6:
                break
            else:
                clear()
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


def menuHapusAnggota():
    while True:
        clear()
        print("+=================+")
        print("|  Hapus Anggota  |")
        print("+=================+")
        try:
            idAnggota = int(input("Masukkan ID Anggota Yang Ingin Dihapus: "))
            if cekIDAnggota(idAnggota):
                query = "DELETE FROM tugas WHERE ID_Anggota = %s"
                cursor.execute(query, (idAnggota, ))
                query = "DELETE FROM anggota WHERE ID_Anggota = %s"
                cursor.execute(query, (idAnggota, ))
                db.commit()
                clear()
                print("+==========================+")
                print("| Anggota Berhasil Dihapus |")
                print("+==========================+")
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+========================================+")
                print("| ID Anggota Tidak Ditemukan Di Database |")
                print("+========================================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except mysql.connector.Error as error:
            clear()
            print(f"Error MySQL: {error}")
            input("Tekan enter untuk melanjutkan...")
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuCariAnggota():
    while True:
        clear()
        print("+==============+")
        print("| Cari Anggota |")
        print("+==============+")
        try:
            idAnggota = int(input("Masukkan ID Anggota Yang Ingin Dicari: "))
            node = anggotaLinkedList.jumpSearchID(idAnggota, "anggota")
            if node:
                clear()
                print("+===================+")
                print("| Anggota Ditemukan |")
                print("+===================+")
                input("Tekan enter untuk melanjutkan...")
                clear()
                dataAnggota = node.data
                tabel = PrettyTable()
                tabel.field_names = ["ID Anggota", "Ranking Anggota", "Nama Anggota", "Keahlian Anggota", "Email Anggota", "Password Anggota"]
                tabel.add_row([dataAnggota["ID_Anggota"], dataAnggota["Rangking_Anggota"], dataAnggota["Nama_Anggota"], dataAnggota["Keahlian_Anggota"], dataAnggota["email_anggota"], dataAnggota["password_anggota"]])
                print(tabel)
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+============================+")
                print("| ID Anggota Tidak Ditemukan |")
                print("+============================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break
def menuUrutkanAnggota():
    while True:
        clear()
        print("+=================+")
        print("| Urutkan Anggota |")
        print("+=================+")
        print("| [1]. Ascending  |")
        print("| [2]. Descending |")
        print("| [3]. Keluar     |")
        print("+=================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
            if pilihan == 1:
                urutkanAnggota("Ascending")
            elif pilihan == 2:
                urutkanAnggota("Descending")
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

def urutkanAnggota(urut):
    clear()
    ambilDataAnggota()
    daftarID = []
    current = anggotaLinkedList.head
    while current:
        daftarID.append(current.data["ID_Anggota"])
        current = current.next
    if urut == "Ascending":
        daftarIDTerurut = anggotaLinkedList.quickSort(daftarID)
    elif urut == "Descending":
        daftarIDTerurut = anggotaLinkedList.quickSortDescending(daftarID)

    tabel = PrettyTable()
    tabel.field_names = ["ID Anggota", "Rangking Anggota", "Nama Anggota", "Keahlian Anggota", "Email Anggota", "Password Anggota"]

    for idAnggota in daftarIDTerurut:
        node = anggotaLinkedList.jumpSearchID(idAnggota, "anggota")
        if node:
            data = node.data
            tabel.add_row([data["ID_Anggota"], data["Rangking_Anggota"], data["Nama_Anggota"], data["Keahlian_Anggota"], data["email_anggota"], data["password_anggota"]])
    
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

# User


def menuBuatUser():
    while True:
        clear()
        print("+=================+")
        print("| Silahkan Daftar |")
        print("+=================+")
        try:
            email = str(input("Masukkan Email: "))
            if email.strip():
                if cekFormatEmail(email):
                    if len(email) <= 100:
                        if not cekEmailUser(email) and not cekEmailAdmin(email) and not cekEmailAdmin(email):
                            password = str(input("Masukkan Password: "))
                            if password.strip():
                                if len(password) <= 255:
                                    nama = str(input("Masukkan Nama: "))
                                    if nama.strip():
                                        if len(nama) <= 255:
                                            alamat = str(input("Masukkan Alamat: "))
                                            if alamat.strip():
                                                if len(alamat) <= 100:
                                                    noHP = str(input("Masukkan Nomor HP: "))
                                                    if noHP.strip():
                                                        if cekFormatNomorHP(noHP):
                                                            if len(noHP) <= 13:
                                                                query = "INSERT INTO user (ID_Admin, Nama_User, Password_User, Email_User, Alamat, No_Hp) VALUES (NULL, %s, %s, %s, %s, %s)"
                                                                cursor.execute(query, (nama, password, email, alamat, noHP))
                                                                db.commit()
                                                                cursor.fetchall()
                                                                clear()
                                                                print("+===========================+")
                                                                print("| Akun User Berhasil Dibuat |")
                                                                print("+===========================+")
                                                                input("Tekan enter untuk melanjutkan...")
                                                                break
                                                            else:
                                                                clear()
                                                                print("+=============================================+")
                                                                print("| Nomor HP Tidak Boleh Lebih Dari 13 Karakter |")
                                                                print("+=============================================+")
                                                                input("Tekan enter untuk melanjutkan...") 
                                                        else:
                                                            clear()
                                                            print("+====================+")
                                                            print("| Format Nomor Salah |")
                                                            print("+====================+")
                                                            input("Tekan enter untuk melanjutkan...")
                                                    else:
                                                        clear()
                                                        print("==============================+")
                                                        print("| Nomor HP Tidak Boleh Kosong |")
                                                        print("==============================+")
                                                        input("Tekan enter untuk melanjutkan...") 
                                                else:
                                                    clear()
                                                    print("+===========================================+")
                                                    print("| Alamat Tidak Boleh Lebih Dari 100 Karakter |")
                                                    print("+===========================================+")
                                                    input("Tekan enter untuk melanjutkan...") 
                                            else:
                                                clear()
                                                print("+===========================+")
                                                print("| Alamat Tidak Boleh Kosong |")
                                                print("+===========================+")
                                                input("Tekan enter untuk melanjutkan...") 
                                        else:
                                            clear()
                                            print("+==========================================+")
                                            print("| Nama Tidak Boleh Lebih Dari 255 Karakter |")
                                            print("+==========================================+")
                                            input("Tekan enter untuk melanjutkan...") 
                                    else:
                                        clear()
                                        print("+=========================+")
                                        print("| Nama Tidak Boleh Kosong |")
                                        print("+=========================+")
                                        input("Tekan enter untuk melanjutkan...")
                                else:
                                    clear()
                                    print("+==============================================+")
                                    print("| Password Tidak Boleh Lebih Dari 255 Karakter |")
                                    print("+==============================================+")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+=============================+")
                                print("| Password Tidak Boleh Kosong |")
                                print("+=============================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+=============================+")
                            print("| Email Sudah Ada Di Database |")
                            print("+=============================+")
                            input("Tekan enter untuk melanjutkan...")
                            break
                    else:
                        clear()
                        print("+===========================================+")
                        print("| Email Tidak Boleh Lebih Dari 100 Karakter |")
                        print("+===========================================+")
                        input("Tekan enter untuk melanjutkan...")
                        break
                else:
                    clear()
                    print("+====================+")
                    print("| Format Email Salah |")
                    print("+====================+")
                    input("Tekan enter untuk melanjutkan...")
                    break
            else:
                clear()
                print("+==========================+")
                print("| Email Tidak Boleh Kosong |")
                print("+==========================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuPerbaruiUser():
    while True:
        clear()
        print("+==============================+")
        print("|         Perbarui User        |")
        print("+==============================+")
        print("| [1]. Perbarui Email User     |")
        print("| [2]. Perbarui Password User  |")
        print("| [3]. Perbarui ID Admin User  |")
        print("| [4]. Perbarui Nama User      |")
        print("| [5]. Perbarui Alamat User    |")
        print("| [6]. Perbarui No HP User     |")
        print("| [7]. Keluar                  |")
        print("+==============================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6/7]: "))
            if pilihan == 1:
                idUser = int(input("Masukkan ID User: "))
                if cekIDUser(idUser):
                    email = str(input("Masukkan Email: "))
                    if email.strip():
                        if cekFormatEmail(email):
                            if len(email) <= 100:
                                if not cekEmailUser(email) and not cekEmailAdmin(email) and not cekEmailAdmin(email):
                                    query = "UPDATE user SET Email_User = %s WHERE ID_User = %s"
                                    cursor.execute(query, (email, idUser))
                                    db.commit()
                                    clear()
                                    print("+============================+")
                                    print("| Email User Berhasil Diubah |")
                                    print("+============================+")
                                    input("Tekan enter untuk melanjutkan...")  
                                else:
                                    clear()
                                    print("+=============================+")
                                    print("| Email Sudah Ada Di Database |")
                                    print("+=============================+")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+===========================================+")
                                print("| Email Tidak Boleh Lebih Dari 100 Karakter |")
                                print("+===========================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+====================+")
                            print("| Format Email Salah |")
                            print("+====================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+==========================+")
                        print("| Email Tidak Boleh Kosong |")
                        print("+==========================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+=====================================+")
                    print("| ID User Tidak Ditemukan Di Database |")
                    print("+=====================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 2:
                idUser = int(input("Masukkan ID User: "))
                if cekIDUser(idUser):
                    passwordUser = str(input("Masukkan Password User Yang Baru: "))
                    if passwordUser.strip():
                        if len(passwordUser) <= 255:
                            query = "UPDATE user SET Password_User = %s WHERE ID_User = %s"
                            cursor.execute(query, (passwordUser, idUser))
                            db.commit()
                            clear()
                            print("+===================================+")
                            print("| Password User Berhasil Diperbarui |")
                            print("+===================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+===================================================+")
                            print("| Password User Tidak Boleh Lebih Dari 255 Karakter |")
                            print("+===================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+==================================+")
                        print("| Password User Tidak Boleh Kosong |")
                        print("+==================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+=====================================+")
                    print("| ID User Tidak Ditemukan Di Database |")
                    print("+=====================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 3:
                idUser = int(input("Masukkan ID User: "))
                if cekIDUser(idUser):
                    idAdmin = int(input("Masukkan ID Admin Yang Baru: "))
                    if str(idAdmin).strip():
                        if cekIDAdmin(idAdmin):
                            if len(str(idAdmin)) <= 11:
                                query = "UPDATE user SET ID_Admin = %s WHERE ID_User = %s"
                                cursor.execute(query, (idAdmin, idUser))
                                db.commit()
                                clear()
                                print("+==============================+")
                                print('| ID Admin Berhasil Diperbarui |')
                                print("+==============================+")
                                input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+=============================================+")
                                print("| ID Admin Tidak Boleh Lebih Dari 11 Karakter |")
                                print("+=============================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+================================+")
                            print("| ID Admin Tidak Ada Di Database |")
                            print("+================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+=============================+")
                        print("| ID Admin Tidak Boleh Kosong |")
                        print("+=============================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+=====================================+")
                    print("| ID User Tidak Ditemukan Di Database |")
                    print("+=====================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 4:
                idUser = int(input("Masukkan ID User: "))
                if cekIDUser(idUser):
                    namaUser = str(input("Masukkan Nama User Yang Baru: "))
                    if namaUser.strip():
                        if len(namaUser) <= 100:
                            query = "UPDATE user SET Nama_User = %s WHERE ID_User = %s"
                            cursor.execute(query, (namaUser, idUser))
                            db.commit()
                            clear()
                            print("+===============================+")
                            print('| Nama User Berhasil Diperbarui |')
                            print("+===============================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+===============================================+")
                            print("| Nama User Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+===============================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+==============================+")
                        print("| Nama User Tidak Boleh Kosong |")
                        print("+==============================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+=====================================+")
                    print("| ID User Tidak Ditemukan Di Database |")
                    print("+=====================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 5:
                idUser = int(input("Masukkan ID User: "))
                if cekIDUser(idUser):
                    alamatUser = str(input("Masukkan Alamat User Yang Baru: "))
                    if alamatUser.strip():
                        if len(alamatUser) <= 100:
                            query = "UPDATE user SET Alamat = %s WHERE ID_User = %s"
                            cursor.execute(query, (alamatUser, idUser))
                            db.commit()
                            clear()
                            print("+=================================+")
                            print('| Alamat User Berhasil Diperbarui |')
                            print("+=================================+")
                            input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+=================================================+")
                            print("| Alamat User Tidak Boleh Lebih Dari 100 Karakter |")
                            print("+=================================================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+================================+")
                        print("| Alamat User Tidak Boleh Kosong |")
                        print("+================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+=====================================+")
                    print("| ID User Tidak Ditemukan Di Database |")
                    print("+=====================================+")
                    input("Tekan enter untuk melanjutkan...")
            elif pilihan == 6:
                idUser = int(input("Masukkan ID User: "))
                if cekIDUser(idUser):
                    noHP = str(input("Masukkan Nomor HP User Yang Baru: "))
                    if noHP.strip():
                        if cekFormatNomorHP(noHP):
                            if len(noHP) <= 13:
                                query = "UPDATE user SET No_Hp = %s WHERE ID_User = %s"
                                cursor.execute(query, (noHP, idUser))
                                db.commit()
                                clear()
                                print("+==============================+")
                                print('| Nomor HP Berhasil Diperbarui |')
                                print("+==============================+")
                                input("Tekan enter untuk melanjutkan...")
                            else:
                                clear()
                                print("+=============================================+")
                                print("| Nomor HP Tidak Boleh Lebih Dari 13 Karakter |")
                                print("+=============================================+")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            clear()
                            print("+==============================+")
                            print("| Nomor HP Tidak Sesuai Format |")
                            print("+==============================+")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+================================+")
                        print("| Alamat User Tidak Boleh Kosong |")
                        print("+================================+")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    clear()
                    print("+=====================================+")
                    print("| ID User Tidak Ditemukan Di Database |")
                    print("+=====================================+")
                    input("Tekan enter untuk melanjutkan...")
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
            input("Tekan enter untuk melanjutkan...")


def menuTampilkanUser():
    clear()
    ambilDataUser()
    tabel = PrettyTable()
    tabel.field_names = ["ID User", "ID Admin", "Nama User", "Email User", "Password User", "Alamat", "No HP"]
    current = userLinkedList.head
    while current:
        data = current.data
        alamat = data["Alamat"]
        if len(alamat) > 50:
            alamat = data["Alamat"][:47] + "..."
        tabel.add_row([data["ID_User"], data["ID_Admin"], data["Nama_User"], data["Email_User"], data["Password_User"], alamat, data["No_Hp"]])
        current = current.next
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

def menuHapusUser():
    while True:
        clear()
        print("+==============+")
        print("|  Hapus User  |")
        print("+==============+")
        try:
            idUser = int(input("Masukkan ID User Yang Ingin Dihapus: "))
            if cekIDUser(idUser):
                idLaporan = ambilIDLaporan(idUser)
                query = "UPDATE admin SET ID_Laporan = %s WHERE ID_Laporan = %s"
                cursor.execute(query, (None, idLaporan))
                query = "DELETE FROM laporan WHERE ID_User = %s"
                cursor.execute(query, (idUser, ))
                query = "DELETE FROM user WHERE ID_User = %s"
                cursor.execute(query, (idUser, ))
                db.commit()
                clear()
                print("+=======================+")
                print("| User Berhasil Dihapus |")
                print("|=======================+")
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+=====================================+")
                print("| ID User Tidak Ditemukan Di Database |")
                print("+=====================================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except mysql.connector.Error as error:
            clear()
            print(f"Error MySQL: {error}")
            input("Tekan enter untuk melanjutkan...")
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuCariUser():
    while True:
        clear()
        print("+===========+")
        print("| Cari User |")
        print("+===========+")
        try:
            idUser = int(input("Masukkan ID User Yang Ingin Dicari: "))
            node = userLinkedList.jumpSearchID(idUser, "user")
            if node:
                clear()
                print("+================+")
                print("| User Ditemukan |")
                print("+================+")
                input("Tekan enter untuk melanjutkan...")
                clear()
                dataAnggota = node.data
                tabel = PrettyTable()
                tabel.field_names = ["ID User", "ID Admin", "Nama User", "Email User", "Password User", "Alamat", "No HP"]
                tabel.add_row([dataAnggota["ID_User"], dataAnggota["ID_Admin"], dataAnggota["Nama_User"], dataAnggota["Email_User"], dataAnggota["Password_User"], dataAnggota["Alamat"], dataAnggota["No_Hp"]])
                print(tabel)
                input("Tekan enter untuk melanjutkan...")
                break
            else:
                clear()
                print("+=========================+")
                print("| ID User Tidak Ditemukan |")
                print("+=========================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def menuUrutkanUser():
    while True:
        clear()
        print("+==================+")
        print("|   Urutkan User   |")
        print("+==================+")
        print("| [1]. Ascending   |")
        print("| [2]. Descending  |")
        print("| [3]. Keluar      |")
        print("+==================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
            if pilihan == 1:
                urutkanUser("Ascending")
            elif pilihan == 2:
                urutkanUser("Descending")
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

def urutkanUser(urut):
    clear()
    ambilDataUser()
    daftarID = []
    current = userLinkedList.head
    while current:
        daftarID.append(current.data["ID_User"])
        current = current.next
    if urut == "Ascending":
        daftarIDTerurut = userLinkedList.quickSort(daftarID)
    elif urut == "Descending":
        daftarIDTerurut = userLinkedList.quickSortDescending(daftarID)

    tabel = PrettyTable()
    tabel.field_names = ["ID User", "ID Admin", "Nama User", "Email User", "Password User", "Alamat", "No HP"]

    for idUser in daftarIDTerurut:
        node = userLinkedList.jumpSearchID(idUser, "user")
        if node:
            data = node.data
            tabel.add_row([data["ID_User"], data["ID_Admin"], data["Nama_User"], data["Email_User"], data["Password_User"], data["Alamat"], data["No_Hp"]])
    
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")


# Ambil Data




def ambilDataTugas():
    try:
        tugasLinkedList.clear()
        query = "SELECT * FROM tugas"
        cursor.execute(query)
        hasil = cursor.fetchall()
        for kolom in hasil:
            dataTugas = {
                "ID_Tugas": kolom[0],
                "ID_Admin": kolom[1],
                "ID_Anggota": kolom[2],
                "Tugas_Laporan": kolom[3],
                "Lokasi_Laporan": kolom[4],
                "status_tugas": kolom[5]
            }
            tugasLinkedList.insert(dataTugas)
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def ambilDataLaporan():
    try:
        laporanLinkedList.clear()
        query = "SELECT * FROM laporan"
        cursor.execute(query)
        hasil = cursor.fetchall()
        for kolom in hasil:
            dataLaporan = {
                "ID_Laporan": kolom[0],
                "ID_User": kolom[1],
                "Isi_Laporan": kolom[2],
                "Lokasi_Laporan": kolom[3],
                "status_laporan": kolom[4],
                "respon_admin": kolom[5]
            }
            laporanLinkedList.insert(dataLaporan)
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def ambilDataAnggota():
    try:
        anggotaLinkedList.clear()
        query = "SELECT * FROM anggota"
        cursor.execute(query)
        hasil = cursor.fetchall()
        for kolom in hasil:
            dataAnggota = {
                "ID_Anggota": kolom[0],
                "Nama_Anggota": kolom[1],
                "Rangking_Anggota": kolom[2],
                "Keahlian_Anggota": kolom[3],
                "password_anggota": kolom[4],
                "email_anggota": kolom[5]
            }
            anggotaLinkedList.insert(dataAnggota)
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def ambilDataUser():
    try:
        userLinkedList.clear()
        query = "SELECT * FROM user"
        cursor.execute(query)
        hasil = cursor.fetchall()
        for kolom in hasil:
            dataUser = {
                "ID_User": kolom[0],
                "ID_Admin": kolom[1],
                "Nama_User": kolom[2],
                "Password_User": kolom[3],
                "Email_User": kolom[4],
                "Alamat": kolom[5],
                "No_Hp": kolom[6]
            }
            userLinkedList.insert(dataUser)
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def ambilIDLaporan(idUser):
    try:
        query = "SELECT * FROM laporan WHERE ID_User = %s"
        cursor.execute(query, (idUser, ))
        login = cursor.fetchone()
        if login:
            cursor.fetchall()
            idLaporan = int(login[0])
            return idLaporan    
        else:
            cursor.fetchall()
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

# Cek

def cekIDLaporan(idLaporan):
    query = "SELECT * FROM laporan WHERE ID_Laporan = %s"
    cursor.execute(query, (idLaporan, ))
    hasil = cursor.fetchone()
    if hasil:
        cursor.fetchall()
        return idLaporan
    else:
        return False

def cekIDUser(idUser):
    query = "SELECT * FROM user WHERE ID_User = %s"
    cursor.execute(query, (idUser, ))
    hasil = cursor.fetchone()
    if hasil:
        cursor.fetchall()
        return idUser
    else:
        return False

def cekIDTugas(idTugas):
    query = "SELECT * FROM tugas WHERE ID_Tugas = %s"
    cursor.execute(query, (idTugas, ))
    hasil = cursor.fetchone()
    if hasil:
        cursor.fetchall()
        return idTugas
    else:
        return False


def cekIDAdmin(idAdmin):
    query = "SELECT * FROM admin WHERE ID_Admin = %s"
    cursor.execute(query, (idAdmin, ))
    hasil = cursor.fetchone()
    if hasil:
        cursor.fetchall()
        return idAdmin
    else:
        cursor.fetchall()
        return False

def cekIDAnggota(idAnggota):
    query = "SELECT * FROM anggota WHERE ID_Anggota = %s"
    cursor.execute(query, (idAnggota, ))
    hasil = cursor.fetchone()
    if hasil:
        cursor.fetchall()
        return idAnggota
    else:
        cursor.fetchall()
        return False

def cekEmailAnggota(emailAnggota):
    try:
        query = "SELECT * FROM anggota WHERE email_anggota = %s"
        cursor.execute(query, (emailAnggota, ))
        user = cursor.fetchone()
        if user:
            cursor.fetchall()
            return True
        else:
            cursor.fetchall()
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def cekEmailAdmin(email):
    try:
        query = "SELECT * FROM admin WHERE email_admin = %s"
        cursor.execute(query, (email, ))
        user = cursor.fetchone()
        if user:
            cursor.fetchall()
            return True
        else:
            cursor.fetchall()
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def cekEmailUser(email):
    try:
        query = "SELECT * FROM user WHERE Email_User = %s"
        cursor.execute(query, (email, ))
        user = cursor.fetchone()
        if user:
            cursor.fetchall()
            return True
        else:
            cursor.fetchall()
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def cekFormatEmail(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def cekFormatNomorHP(noHP):
    pattern = r"^08[0-9]+$"
    if re.match(pattern, noHP):
        return True
    else:
        return False