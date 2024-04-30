# Dokumentasi PA A23 KELOMPOK 10

## A. Deskripsi Program

Program Pelayanan Konsultasi Terkait Energi yang Tersedia dibuat dengan tujuan untuk membantu masyarakat, organisasi, dan industri dalam meenghadapi tantangan eneergi bersih dan terjangkau yang tersedia di lingkungan. Selain itu, layanan program ini juga memiliki tujuan-tujuan kunci yaitu: memberikan pemahaman yang lebih baik kepada masyarakat tentang energi bersih dan terjangkau, meliputi sumber energi terbarukan, teknologi yang digunakan, dan manfaatnya bagi lingkungan dan ekonomi. Selain itu, program juga menyediakan solusi praktis dan inovatif untuk masalah energi yang dihadapi oleh klien, seperti memberikan rekomendasi penanganan untuk meningkatkan efisiensi energi dan mengurangi biaya. Program ini juga membantu klien dalam mengoptimalkan penggunaan energi dengan mengidentifikasi area-area di mana efisiensi dapat ditingkatkan dan memberikan langkah-langkah praktis untuk mencapai tujuan tersebut. Selain itu, program ini juga mendukung klien dalam pengambilan keputusan terkait investasi dalam teknologi energi bersih dan terjangkau, dengan memberikan informasi yang objektif, analisis komprehensif, dan rekomendasi yang sesuai. Terakhir, program ini juga mengedukasi dan membimbing masyarakat untuk menjadi lebih sadar akan pentingnya energi bersih dan terjangkau, serta mendorong partisipasi aktif dalam mengadopsi solusi-solusi energi yang ramah lingkungan.. Dengan begitu, program ini diharapkan dapat meningkatkan efektivitas dan efisiensi dalam memberikan bantuan kepada pihak manapu terkait Energi Bersih.

Program ini dibuat dengan menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List. Program "Layanan konsultasi terkait Energi yang Tersedia" ini juga menggunakan sebuah database, yaitu database MySQL yang digunakan untuk menyimpan data dan informasi setiap entitas yang terlibat sehingga program dapat melakukan berbagai operasi manipulasi data dengan efisien, serta mendukung kinerja layanan secara keseluruhan.

## B. Struktur Project
1. **Folder Controller:** berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.

   - admin controller: Mengatur logika terkait dengan admin, seperti manajemen User, manajemen laporan, manajemen tugas, dan operasi administratif lainnya.
   - anggota controller: Mengelola operasi terkait anggota, seperti pendaftaran anggota, menampilkan tugas, konfirmasi tugas, dan aktivitas lainnya.
   - auth controller: Menangani proses otentikasi dan ototorisasi baik user maupun admin untuk akses ke bagian-bagian tertentu pada program.
   - linkedlist controller: Mengatur operasi yang terkait dengan struktur data linked list, seperti penambahan, penghapusan, dan manipulasi data lain pada linked list.
   - user controller: Bertanggung jawab untuk interaksi antara pengguna dengan program, termasuk proses input data seperti laporan dan mengecek laporan, dan hal lain.

2. **Folder Model:** berisi file-file model yang berisi fungsi-fungsi untuk mengakses database dan memproses data, serta berfungsi merepresentasikan struktur data program.
   
   - database: Berisi definisi struktur database dan koneksi ke basis data agar terhubung ke database, dalam hal ini MySQL.

3. **Folder View:**  berisi file-file view yang berisi tampilan antarmuka aplikasi yang akan dilihat oleh pengguna tanpa melakukan pemrosesan data atau logika.

   - admin view: Menampilkan antarmuka untuk admin, termasuk menu admin seperti laporan, tugas, user, CRUD admin, dan lain lain.
   - anggota view: Berisi tampilan yang ditujukan untuk anggota, seperti tampilkan tugas, konfirmasi tugas, dan lain-lain.
   - main view: Merupakan tampilan utama yang menampilkan berbagai menu yang muncul diawal pada saat program pertama kali dijalankan, seperti login, daftar, dan lain-lain.
   - user view: Menampilkan antarmuka untuk user, termasuk buat laporan, cek laporan dan lain-lain. 

4. **File main.py:** Merupakan file utama yang menghubungkan komponen-komponen MVC sehingga menghubungkan antara model, view, dan controller.

## C. Fitur dan Fungsionalitas

## Fitur

Pada program ini terdapat library yang digunakan, diantaranya adalah PrettyTable, math, mysql.connector, os, re.

1. **math**: merupakan Library yang menyediakan fungsi-fungsi matematika seperti sqrt() (akar kuadrat), sin() (sinus), cos() (kosinus), dan lain-lain. Digunakan untuk operasi matematika dalam program.
2. **prettytable**: adalah Library yang digunakan untuk membuat tabel yang rapi dan terstruktur di konsol. Berguna untuk menampilkan data dalam format tabel yang mudah dibaca.
3. **mysql.connector**: yaitu Library yang digunakan untuk menghubungkan dan berinteraksi dengan database MySQL. Memungkinkan program untuk melakukan query dan manipulasi data pada database MySQL.
4. **os**: menyediakan fungsi-fungsi yang berkaitan dengan sistem operasi seperti mengakses variabel lingkungan dan berinteraksi dengan sistem berkas. Berguna untuk operasi-operasi yang terkait dengan sistem operasi seperti mengakses direktori, mengatur variabel lingkungan, dan lain-lain.
5. **re**: Library ini digunakan untuk operasi-operasi regular expression seperti pencocokan pola dalam teks. Berguna untuk mencari dan memanipulasi teks berdasarkan pola tertentu.

Beberapa fitur yang terdapat dalam program meliputi:

- **User**
  1. Buat Laporan: user dapat membuat laporan terkait Layanan Konsultasi Energi
  2. Cek Laporan: user dapat mengecek laporan yang sudah dia buat
  3. Keluar: user dapat kembali ke Menu utama
   
- ** Admin**
  1. Laporan: admin dapat melakukan beberapa manajemen terkait Laporan, seperti CRUD Laporan, search laporan, dan sorting laporan.
  2. Tugas: admin dapat melakukan beberapa manajemen terkait tugas, seperti melakukan CRUD tugas, search tugas, dan sorting tugas.
  3. Anggota: admin dapat melakukan beberapa manajemen terkait admin, seperti melakukan CRUD admin, search admin, dan sorting admin.
  4. User: admin dapat melakukan beberapa manajemen terkait user, seperti melakukan CRUD User, search User, dan sorting user.
  5. Keluar: admin dapat kembali ke Menu Utama.

- **Anggota**
  1. Tampilkan Tugas: Anggota dapat menampilkan tugas yang di berikan kepada dia terkait Laporan user
  2. Konfirmasi Tugas: Anggota dapat mengubah status tugas yang awalnya pending menjadi selesai atau sudah dikerjakan
  3. Keluar: Anggota dapat kembali ke Menu Utama

## D. Cara Penggunaan
1. Saat program pertama kali dimulai, program akan menampilkan menu utama yang terdiri atas 3 menu, yaitu 1) login, 2) daftar, 3) keluar.
2. Jika belum mempunyai akun maka melakukan opsi 2 yaitu daftar, saat mendaftar maka user akan menginput Email, Password, Nama, Alamat, dan NO HP.
3. Jika sudah memiliki akun, maka melakukan opsi 1 yaitu login, terdapat 3 macam login sebagai pengguna apa kita ingin login. Bisa sebagai Admin, Anggota, dan User. Setiap pengguna memiliki menu yang berbeda beda.
4. Pada User terdapat 3 menu, yaitu Buat Laporan, Cek Laporan, dan Keluar.
5. Pada Anggota terdapat 3 menu, yaitu Tampilkan Tugas, Konfirmasi Tugas, dan Keluar.
6. Pada Admin terdapat 5 menu, yaitu Laporan, Tugas, Anggota, User, dan Keluar. Dimana pada tiap menu tersebut kecuali keluar, admin bisa melakukan CRUD, searching, dan sorting.
7. Terakhir, Opsi 3 yaitu Keluar, membuat program selesai apabila sudah digunakan.
