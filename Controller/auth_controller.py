from Model.database import koneksiDatabase
from View import auth_view as auth
import mysql.connector
import os
import re

db, cursor = koneksiDatabase()
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Login

def loginAdmin(email, password):
    try:
        cursor.fetchall()
        query = "SELECT * FROM admin WHERE email_admin = %s AND Password_Admin = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def loginAnggota(email, password):
    try:
        cursor.fetchall()
        query = "SELECT * FROM anggota WHERE email_anggota = %s AND password_anggota = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def loginUser(email, password):
    try:
        cursor.fetchall()
        query = "SELECT * FROM user WHERE Email_User = %s AND Password_User = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def ambilNamaAnggota(email, password):
    try:
        query = "SELECT * FROM anggota WHERE email_anggota = %s AND password_anggota = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            namaAnggota = str(login[1])
            cursor.fetchall()
            return namaAnggota
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def ambilNamaUser(email, password):
    try:
        query = "SELECT * FROM user WHERE Email_User = %s AND Password_User = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            namaAnggota = str(login[2])
            cursor.fetchall()
            return namaAnggota
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")
# Daftar

def daftarEmail():
    while True:
        email = str(input("Masukkan Email: "))
        if cekFormatEmail(email):
            if not cekEmailAdmin(email):
                if not cekEmailAnggota(email):
                    if not cekEmailUser(email):
                            if len(email) <= 100:
                                return email
                            else:
                                clear()
                                print("+===========================================+")
                                print("| Email Tidak Boleh Lebih Dari 100 Karakter |")
                                print("+===========================================+")
                                input("Tekan enter untuk melanjutkan...")
                    else:
                        clear()
                        print("+===================================+")
                        print("| Email Sudah Terdaftar Di Database |")
                        print("+===================================+")
                        input("Tekan enter untuk melanjutkan...")
                        clear()
                        cursor.fetchall()
                        print("+=============================+")
                        print("|   Apakah anda ingin Login?  |")
                        print("+=============================+")
                        print("| [1]. Ya                     |")
                        print("| [2]. Tidak                  |")
                        print("+=============================+")
                        pilihan = int(input("Masukkan Pilihan [1/2]: "))
                        if pilihan == 1:
                            auth.login()
                            return False
                        elif pilihan == 2:
                            return False
                        else:
                            clear()
                            print("+================================+")
                            print("|  Inputan Tidak Ada Di Pilihan  |")
                            print("| Anda Dikembalikan Ke Menu Awal |")
                            print("+================================+")
                            input("Tekan enter untuk melanjutkan...")
                            return False
                else:
                    clear()
                    print("+===================================+")
                    print("| Email Sudah Terdaftar Di Database |")
                    print("+===================================+")
                    input("Tekan enter untuk melanjutkan...")
                    clear()
                    cursor.fetchall()
                    print("+=============================+")
                    print("|   Apakah anda ingin Login?  |")
                    print("+=============================+")
                    print("| [1]. Ya                     |")
                    print("| [2]. Tidak                  |")
                    print("+=============================+")
                    pilihan = int(input("Masukkan Pilihan [1/2]: "))
                    if pilihan == 1:
                        auth.login()
                        return False
                    elif pilihan == 2:
                        return False
                    else:
                        clear()
                        print("+================================+")
                        print("|  Inputan Tidak Ada Di Pilihan  |")
                        print("| Anda Dikembalikan Ke Menu Awal |")
                        print("+================================+")
                        input("Tekan enter untuk melanjutkan...")
                        return False
            else:
                clear()
                print("+===================================+")
                print("| Email Sudah Terdaftar Di Database |")
                print("+===================================+")
                input("Tekan enter untuk melanjutkan...")
                clear()
                cursor.fetchall()
                print("+=============================+")
                print("|   Apakah anda ingin Login?  |")
                print("+=============================+")
                print("| [1]. Ya                     |")
                print("| [2]. Tidak                  |")
                print("+=============================+")
                pilihan = int(input("Masukkan Pilihan [1/2]: "))
                if pilihan == 1:
                    auth.login()
                    return False
                elif pilihan == 2:
                    return False
                else:
                    clear()
                    print("+================================+")
                    print("|  Inputan Tidak Ada Di Pilihan  |")
                    print("| Anda Dikembalikan Ke Menu Awal |")
                    print("+================================+")
                    input("Tekan enter untuk melanjutkan...")
                    return False
        else:
            clear()
            print("+===========================+")
            print("| Email Tidak Sesuai Format |")
            print("+===========================+")
            return False
    
def daftarNama():
    while True:
        nama = str(input("Masukkan Nama: "))
        if len(nama) <= 255:
            return nama
        else:
            clear()
            print("+==========================================+")
            print("| Nama Tidak Boleh Lebih Dari 255 Karakter |")
            print("+==========================================+")

def daftarPassword():
    while True:
        password = str(input("Masukkan Password: "))
        if len(password) <= 255:
            return password
        else:
            clear()
            print("+==========================================+")
            print("| Nama Tidak Boleh Lebih Dari 255 Karakter |")
            print("+==========================================+")
            input("Tekan enter untuk melanjutkan...") 

def daftarAlamat():
    while True:
        alamat = str(input("Masukkan Alamat: "))
        if len(alamat) <= 100:
            return alamat
        else:
            clear()
            print("+===========================================+")
            print("| Alamat Tidak Boleh Lebih Dari 100 Karakter |")
            print("+===========================================+")
            input("Tekan enter untuk melanjutkan...") 

def daftarNoHP():
    while True:
        noHP = str(input("Masukkan Nomor HP: "))
        if len(noHP) <= 20:
            return noHP
        else:
            clear()
            print("+==============================================+")
            print("| Nomor HP Tidak Boleh Lebih Dari 20 Karakter |")
            print("+=============================================+")
            input("Tekan enter untuk melanjutkan...") 

# Cek

def cekNamaAdmin(nama):
    try:
        query = "SELECT * FROM admin WHERE Nama_Admin = %s"
        cursor.execute(query, (nama, ))
        admin = cursor.fetchone()
        if admin:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def cekNamaAnggota(nama):
    try:
        query = "SELECT * FROM anggota WHERE Nama_Anggota = %s"
        cursor.execute(query, (nama, ))
        admin = cursor.fetchone()
        if admin:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def cekNamaUser(nama):
    try:
        query = "SELECT * FROM user WHERE Nama_User = %s"
        cursor.execute(query, (nama, ))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def cekFormatEmail(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def cekEmailUser(email):
    try:
        query = "SELECT * FROM user WHERE Email_User = %s"
        cursor.execute(query, (email, ))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def cekEmailAnggota(email):
    try:
        query = "SELECT * FROM anggota WHERE email_anggota = %s"
        cursor.execute(query, (email, ))
        user = cursor.fetchone()
        if user:
            return True
        else:
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
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")