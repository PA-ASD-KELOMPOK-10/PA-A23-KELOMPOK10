from Model.database import koneksiDatabase
from Controller import linkedlist_controller as linkedlist
from prettytable import PrettyTable
import mysql.connector
import os

tugasLinkedList = linkedlist.LinkedList()

db, cursor = koneksiDatabase()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuAnggotaTampilkanTugas(nama):
    ambilDataTugasAnggota(nama)
    tabel = PrettyTable()
    tabel.field_names = ["ID Tugas", "Tugas Laporan", "Lokasi Laporan", "Status Tugas"]
    current = tugasLinkedList.head
    while current:
        data = current.data
        tabel.add_row([data["ID_Tugas"], data["Tugas_Laporan"], data["Lokasi_Laporan"], data["status_tugas"]])
        current = current.next
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

def menuAnggotaKonfirmasiTugas(nama):
    query = "SELECT ID_Anggota FROM anggota WHERE Nama_Anggota = %s"
    cursor.execute(query, (nama, ))
    hasilID = cursor.fetchone()
    if hasilID:
        idTugas = int(input("Masukkan ID Tugas: "))
        if cekIDTugasAnggota(idTugas, hasilID):
            ambilDataTugasAnggotaIDTugas(hasilID, idTugas)
            tabel = PrettyTable()
            tabel.field_names = ["ID Tugas", "Tugas Laporan", "Lokasi Laporan", "Status Tugas"]
            current = tugasLinkedList.head
            while current:
                data = current.data
                tabel.add_row([data["ID_Tugas"], data["Tugas_Laporan"], data["Lokasi_Laporan"], data["status_tugas"]])
                current = current.next
            clear()
            print(tabel)
            statusTugas = str(input("Masukkan Status Tugas Yang Baru: "))
            query = "UPDATE tugas SET status_tugas = %s WHERE ID_tugas = %s"
            cursor.execute(query, (statusTugas, idTugas))
            db.commit()
            clear()
            print("+==============================+")
            print("| Status Tugas Berhasil Diubah |")
            print("+==============================+")
            input("Tekan enter untuk melanjutkan...")

        else:
            clear()
            print("+==========================+")
            print("| ID Tugas Tidak Ditemukan |")
            print("+==========================+")
            input("Tekan enter untuk melanjutkan...")
    else:
        clear()
        print("+============================+")
        print("| ID Anggota Tidak Ditemukan |")
        print("+============================+")
        input("Tekan enter untuk melanjutkan...")

def cekIDTugasAnggota(idTugas, hasilID):
    idAnggota = int(hasilID[0])
    query = "SELECT * FROM tugas WHERE ID_Tugas = %s AND ID_Anggota = %s"
    cursor.execute(query, (idTugas, idAnggota))
    hasil = cursor.fetchone()
    if hasil:
        cursor.fetchall()
        return idTugas
    else:
        return False

def ambilDataTugasAnggota(nama):
    try:
        query = "SELECT ID_Anggota FROM anggota WHERE Nama_Anggota = %s"
        cursor.execute(query, (nama, ))
        hasilID = cursor.fetchone()
        if hasilID:
            tugasLinkedList.clear()
            idAnggota = int(hasilID[0])
            cursor.fetchall()
            query = "SELECT ID_Tugas, Tugas_Laporan, Lokasi_Laporan, status_tugas FROM tugas WHERE ID_Anggota = %s"
            cursor.execute(query, (idAnggota, ))
            hasil = cursor.fetchall()
            for kolom in hasil:
                dataTugas = {
                    "ID_Tugas": kolom[0],
                    "Tugas_Laporan": kolom[1],
                    "Lokasi_Laporan": kolom[2],
                    "status_tugas":kolom[3]
                }
                tugasLinkedList.insert(dataTugas)
        else:
            print("+============================+")
            print("| ID Anggota Tidak Ditemukan |")
            print("+============================+")
            input("Tekan enter untuk melanjutkan...")

    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def ambilDataTugasAnggotaIDTugas(hasilID, idTugas):
    tugasLinkedList.clear()
    idAnggota = int(hasilID[0])
    cursor.fetchall()
    query = "SELECT ID_Tugas, Tugas_Laporan, Lokasi_Laporan, status_tugas FROM tugas WHERE ID_Anggota = %s AND ID_Tugas = %s"
    cursor.execute(query, (idAnggota, idTugas))
    hasil = cursor.fetchall()
    for kolom in hasil:
        dataTugas = {
            "ID_Tugas": kolom[0],
            "Tugas_Laporan": kolom[1],
            "Lokasi_Laporan": kolom[2],
            "status_tugas":kolom[3]
        }
        tugasLinkedList.insert(dataTugas)
