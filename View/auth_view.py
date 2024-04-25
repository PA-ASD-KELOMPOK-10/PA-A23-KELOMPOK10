import os
from Controller import auth_controller as auth
from Model.database import koneksiDatabase
from View import anggota_view as anggota
from View import user_view as user
from View import admin_view as admin

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
            if auth.cekFormatEmail(email):
                if auth.cekEmailAdmin(email):
                    password = str(input("Masukkan Password: "))
                    if auth.loginAdmin(email, password):
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
                        cursor.fetchall()
                        break
                elif auth.cekEmailAnggota(email):
                    password = str(input("Masukkan Password: "))
                    if auth.loginAnggota(email, password):
                        clear()
                        print("+================+")
                        print("| Login Berhasil |")
                        print("+================+")
                        input("Tekan enter untuk melanjutkan...")
                        nama = auth.ambilNamaAnggota(email, password)
                        anggota.menuAnggota(nama)
                        break
                    else:
                        clear()
                        print("+================+")
                        print("| Password Salah |")
                        print("+================+")
                        input("Tekan enter untuk melanjutkan...")
                        cursor.fetchall()
                        break
                elif auth.cekEmailUser(email):
                    password = str(input("Masukkan Password: "))
                    if auth.loginUser(email, password):
                        clear()
                        print("+================+")
                        print("| Login Berhasil |")
                        print("+================+")
                        input("Tekan enter untuk melanjutkan...")
                        nama = auth.ambilNamaUser(email, password)
                        user.menuUser(nama)
                        break
                    else:
                        clear()
                        print("+================+")
                        print("| Password Salah |")
                        print("+================+")
                        input("Tekan enter untuk melanjutkan...")
                        cursor.fetchall()
                        break
                else:
                    clear()
                    print("+===============================+")
                    print("|  Email Tidak Ada Di Database  |")
                    print("+===============================+")
                    input("Tekan enter untuk melanjutkan...")
                    clear()
                    print("+=============================+")
                    print("|  Apakah anda ingin daftar?  |")
                    print("+=============================+")
                    print("| [1]. Ya                     |")
                    print("| [2]. Tidak                  |")
                    print("+=============================+")
                    pilihan = int(input("Masukkan Pilihan [1/2]: "))
                    if pilihan == 1:
                        daftar()
                        break
                    elif pilihan == 2:
                        break
                    else:
                        clear()
                        print("+================================+")
                        print("|  Inputan Tidak Ada Di Pilihan  |")
                        print("| Anda Dikembalikan Ke Menu Awal |")
                        print("+================================+")
                        input("Tekan enter untuk melanjutkan...")
                        break
            else:
                clear()
                print("+===========================+")
                print("| Email Tidak Sesuai Format |")
                print("+===========================+")
                input("Tekan enter untuk melanjutkan...")

        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")

def daftar():
    while True:
        clear()
        print("+=================+")
        print("| Silahkan Daftar |")
        print("+=================+")
        try:
            email = auth.daftarEmail()
            if email:
                password = auth.daftarPassword()
                if password:
                    nama = auth.daftarNama()
                    if nama:
                        alamat = auth.daftarAlamat()
                        if alamat:
                            noHP = auth.daftarNoHP()
                            if noHP:
                                query = "INSERT INTO user (ID_Admin, Nama_User, Password_User, Email_User, Alamat, No_Hp) VALUES (NULL, %s, %s, %s, %s, %s)"
                                cursor.execute(query, (nama, password, email, alamat, noHP))
                                db.commit()
                                clear()
                                pesan = f"| Akun Dengan Nama {nama} Berhasil Terdaftar |"
                                print("+" + "=" * (len(pesan) - 2) + "+")
                                print(pesan)
                                print("+" + "=" * (len(pesan) - 2) + "+")
                                input("Tekan enter untuk melanjutkan...")
                                break
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                break
        except:
            clear()
            print("+===========================+")
            print("| Mohon Perhatikan Masukkan |")
            print("+===========================+")
            input("Tekan enter untuk melanjutkan...")