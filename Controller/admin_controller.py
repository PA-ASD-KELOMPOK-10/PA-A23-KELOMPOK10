from Model.database import koneksiDatabase
from Controller import linkedlist_controller as linkedlist
from prettytable import PrettyTable
import mysql.connector
import os
db, cursor = koneksiDatabase()

tugasLinkedList = linkedlist.LinkedList()
laporanLinkedList = linkedlist.LinkedList()

def clear():
    os.system("cls" if os.name == "nt" else "clear")



# Laporan



def menuBuatLaporan():
    while True:
        clear()
        print("+==============+")
        print("| Buat Laporan |")
        print("+==============+")
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

def menuTampilkanLaporan():
    ambilDataLaporan()
    tabel = PrettyTable()
    tabel.field_names = ["ID Laporan", "ID User", "Isi Laporan", "Lokasi Laporan", "Status Laporan", "Respon Admin"]
    current = laporanLinkedList.head
    while current:
        data = current.data
        tabel.add_row([data["ID_Laporan"], data["ID_User"], data["Isi_Laporan"], data["Lokasi_Laporan"], data["status_laporan"], data["respon_admin"]])
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
        pilihan = int(input("Masukkan Pilihan [1/2/3/4/5/6]: "))
        if pilihan == 1:
            idLaporan = int(input("Masukkan ID Laporan: "))
            if cekIDLaporan(idLaporan):
                idUser = int(input("Masukkan ID User Yang Baru: "))
                if str(idUser).strip():
                    if cekIDUser(idUser):
                        query = "UPDATE laporan SET ID_User = %s WHERE ID_Laporan = %s"
                        cursor.execute(query, (idUser, idLaporan))
                        clear()
                        print("+=========================+")
                        print("| ID User Berhasil Dibuah |")
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

def menuHapusLaporan():
    while True:
        clear()
        print("+=================+")
        print("|  Hapus Laporan  |")
        print("+=================+")
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

def menuCariLaporan():
    while True:
        clear()
        print("+==============+")
        print("| Cari Laporan |")
        print("+==============+")
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
            tabel.field_names = ["ID Laporan", "ID User", "Isi Laporan", "Lokasi Laporan"]
            tabel.add_row([dataLaporan["ID_Laporan"], dataLaporan["ID_User"], dataLaporan["Isi_Laporan"], dataLaporan["Lokasi_Laporan"]])
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

def menuUrutkanLaporan():
    clear()
    ambilDataLaporan()
    daftarID = []
    current = laporanLinkedList.head
    while current:
        daftarID.append(current.data["ID_Laporan"])
        current = current.next
    
    daftarIDTerurut = laporanLinkedList.quickSort(daftarID)
    
    tabel = PrettyTable()
    tabel.field_names = ["ID Laporan", "ID User", "Isi Laporan", "Lokasi Laporan"]

    for idLaporan in daftarIDTerurut:
        node = laporanLinkedList.jumpSearchID(idLaporan, "laporan")
        if node:
            data = node.data
            tabel.add_row([data["ID_Laporan"], data["ID_User"], data["Isi_Laporan"], data["Lokasi_Laporan"]])
    
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")



# Tugas



def menuBuatTugas():
    while True:
        print("+==============+")
        print("|  Buat Tugas  |")
        print("+==============+")
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

def menuTampilkanTugas():
    ambilDataTugas()
    tabel = PrettyTable()
    tabel.field_names = ["ID Tugas", "ID Admin", "ID Anggota", "Tugas Laporan", "Lokasi Laporan", "Status Tugas"]
    current = tugasLinkedList.head
    while current:
        data = current.data
        tabel.add_row([data["ID_Tugas"], data["ID_Admin"], data["ID_Anggota"], data["Tugas_Laporan"], data["Lokasi_Laporan"], data["status_tugas"]])
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

def menuHapusTugas():
    while True:
        clear()
        print("+===============+")
        print("|  Hapus Tugas  |")
        print("+===============+")
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

def menuCariTugas():
    while True:
        clear()
        print("+============+")
        print("| Cari Tugas |")
        print("+============+")
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

def menuUrutkanTugas():
    clear()
    ambilDataTugas()
    daftarID = []
    current = tugasLinkedList.head
    while current:
        daftarID.append(current.data["ID_Tugas"])
        current = current.next

    daftarIDTerurut = tugasLinkedList.quickSort(daftarID)

    tabel = PrettyTable()
    tabel.field_names = ["ID Tugas", "ID Admin", "ID Anggota", "Tugas Laporan", "Lokasi Laporan", "Status Tugas"]

    for idTugas in daftarIDTerurut:
        node = tugasLinkedList.jumpSearchID(idTugas, "tugas")
        if node:
            data = node.data
            tabel.add_row([data["ID_Tugas"], data["ID_Admin"], data["ID_Anggota"], data["Tugas_Laporan"], data["Lokasi_Laporan"], data["status_tugas"]])

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