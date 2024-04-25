from Model.database import koneksiDatabase
from prettytable import PrettyTable
import mysql.connector
import os

db, cursor = koneksiDatabase()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuBuatLaporan(nama):
    while True:
        clear()
        print("+==============+")
        print("| Menu Laporan |")
        print("+==============+")
        idUser = simpanIDUser(nama)
        isiLaporan = str(input("Masukkan Isi Laporan: "))
        if len(isiLaporan) <= 500:
            lokasiLaporan = str(input("Masukkan Lokasi: "))
            if len(lokasiLaporan) <= 100:
                try:
                    query = "INSERT INTO laporan (ID_User, Isi_Laporan, Lokasi_Laporan) VALUES (%s, %s, %s)"
                    cursor.execute(query, (idUser, isiLaporan, lokasiLaporan))
                    db.commit()
                    clear()
                    print("+==========================+")
                    print("| Laporan Berhasil Dibuat! |")
                    print("+==========================+")
                    input("Tekan enter untuk melanjutkan...")
                    break
                except mysql.connector.Error as err:
                    print(f"Error MySQL: {err.msg}")
                    input("Tekan enter untuk melanjutkan...")
            else:
                clear()
                print("+====================================================+")
                print("| Lokasi Laporan Tidak Boleh Lebih Dari 100 Karakter |")
                print("+====================================================+")
                input("Tekan enter untuk melanjutkan...") 
                cursor.fetchall()
        else:
            print("+=================================================+")
            print("| Isi Laporan Tidak Boleh Lebih Dari 500 Karakter |")
            print("+=================================================+")
            input("Tekan enter untuk melanjutkan...") 
            cursor.fetchall()

def menuCekLaporan(nama):
    clear()
    idUser = simpanIDUser(nama)
    query = "SELECT * FROM laporan WHERE ID_User = %s"
    cursor.execute(query, (idUser, ))
    hasil = cursor.fetchall()
    tabel = PrettyTable()
    tabel.field_names = [desc[0] for desc in cursor.description]
    for kolom in hasil:
        tabel.add_row(kolom)
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

def simpanIDUser(nama):
    namaUser = nama
    query = "SELECT ID_User FROM user WHERE Nama_User = %s"
    cursor.execute(query, (namaUser, ))
    hasil = cursor.fetchone()
    if hasil:
        idUser = hasil[0]
        return idUser