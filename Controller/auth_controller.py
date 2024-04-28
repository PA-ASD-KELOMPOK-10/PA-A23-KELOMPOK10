from Model.database import koneksiDatabase
from View import admin_view as admin
from View import anggota_view as anggota
from View import user_view as user
import mysql.connector
import os
import re

db, cursor = koneksiDatabase()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def login():
    while True:
        clear()
        print("+================+")
        print("| Silahkan Login |")
        print("+================+")
        try:
            email = str(input("Masukkan Email: "))
            if cekEmailAdmin(email):
                password = str(input("Masukkan Password: "))
                if loginAdmin(email, password):
                    clear()
                    print("+================+")
                    print("| Login Berhasil |")
                    print("+================+")
                    input("Tekan enter untuk melanjutkan...")
                    admin.menuAdmin()
                    break
                else:
                    clear()
                    print("+================+")
                    print("| Password Salah |")
                    print("+================+")
                    input("Tekan enter untuk melanjutkan...")
            elif cekEmailAnggota(email):
                password = str(input("Masukkan Password: "))
                if loginAnggota(email, password):
                    clear()
                    print("+================+")
                    print("| Login Berhasil |")
                    print("+================+")
                    input("Tekan enter untuk melanjutkan...")
                    anggota.menuAnggota(ambilNamaAnggota(email, password))
                    break
                else:
                    clear()
                    print("+================+")
                    print("| Password Salah |")
                    print("+================+")
                    input("Tekan enter untuk melanjutkan...")
            elif cekEmailUser(email):
                password = str(input("Masukkan Password: "))
                if loginUser(email, password):
                    clear()
                    print("+================+")
                    print("| Login Berhasil |")
                    print("+================+")
                    input("Tekan enter untuk melanjutkan...")
                    user.menuUser(ambilNamaUser(email, password))
                    break
                else:
                    clear()
                    print("+================+")
                    print("| Password Salah |")
                    print("+================+")
                    input("Tekan enter untuk melanjutkan...")
            else:
                clear()
                print("+=======================+")
                print("| Email tidak terdaftar |")
                print("+=======================+")
                input("Tekan enter untuk melanjutkan...")
                break
        except:
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")
            break

def daftar():
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
                                                                clear()
                                                                pesan = f"| Akun Dengan Nama {nama} Berhasil Terdaftar |"
                                                                print("+" + "=" * (len(pesan) - 2) + "+")
                                                                print(pesan)
                                                                print("+" + "=" * (len(pesan) - 2) + "+")
                                                                input("Tekan enter untuk melanjutkan...")
                                                                cursor.fetchall()
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

def loginAdmin(email, password):
    try:
        query = "SELECT * FROM admin WHERE email_admin = %s AND Password_Admin = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            cursor.fetchall()
            return True
        else:
            cursor.fetchall()
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def loginAnggota(email, password):
    try:
        query = "SELECT * FROM anggota WHERE email_anggota = %s AND password_anggota = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            cursor.fetchall()
            return True
        else:
            cursor.fetchall()
            return False
    except mysql.connector.Error as err:
        print(f"Error MySQL: {err.msg}")
        input("Tekan enter untuk melanjutkan...")

def loginUser(email, password):
    try:
        query = "SELECT * FROM user WHERE Email_User = %s AND Password_User = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            cursor.fetchall()
            return True
        else:
            cursor.fetchall()
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

def ambilNamaAnggota(email, password):
    try:
        query = "SELECT * FROM anggota WHERE email_anggota = %s AND password_anggota = %s"
        cursor.execute(query, (email, password))
        login = cursor.fetchone()
        if login:
            cursor.fetchall()
            namaAnggota = str(login[1])
            return namaAnggota
        else:
            cursor.fetchall()
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
            cursor.fetchall()
            namaAnggota = str(login[2])
            return namaAnggota
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
