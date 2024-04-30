# PA-A23-KELOMPOK10

A. Deskripsi Program

Program Pelayanan Konsultasi Terkait Energi yang Tersedia dibuat dengan tujuan untuk membantu masyarakat, organisasi, dan industri dalam meenghadapi tantangan eneergi bersih dan terjangkau yang tersedia di lingkungan. Selain itu, layanan program ini juga memiliki tujuan-tujuan kunci yaitu: memberikan pemahaman yang lebih baik kepada masyarakat tentang energi bersih dan terjangkau, meliputi sumber energi terbarukan, teknologi yang digunakan, dan manfaatnya bagi lingkungan dan ekonomi. Selain itu, program juga menyediakan solusi praktis dan inovatif untuk masalah energi yang dihadapi oleh klien, seperti memberikan rekomendasi penanganan untuk meningkatkan efisiensi energi dan mengurangi biaya. Program ini juga membantu klien dalam mengoptimalkan penggunaan energi dengan mengidentifikasi area-area di mana efisiensi dapat ditingkatkan dan memberikan langkah-langkah praktis untuk mencapai tujuan tersebut. Selain itu, program ini juga mendukung klien dalam pengambilan keputusan terkait investasi dalam teknologi energi bersih dan terjangkau, dengan memberikan informasi yang objektif, analisis komprehensif, dan rekomendasi yang sesuai. Terakhir, program ini juga mengedukasi dan membimbing masyarakat untuk menjadi lebih sadar akan pentingnya energi bersih dan terjangkau, serta mendorong partisipasi aktif dalam mengadopsi solusi-solusi energi yang ramah lingkungan.. Dengan begitu, program ini diharapkan dapat meningkatkan efektivitas dan efisiensi dalam memberikan bantuan kepada pihak manapu terkait Energi Bersih.

Program ini dibuat dengan menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List. Program "Layanan konsultasi terkait Energi yang Tersedia" ini juga menggunakan sebuah database, yaitu database MySQL yang digunakan untuk menyimpan data dan informasi setiap entitas yang terlibat sehingga program dapat melakukan berbagai operasi manipulasi data dengan efisien, serta mendukung kinerja layanan secara keseluruhan.

B. Struktur Project
1. *Folder Controller:* berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.

   - admin controller: Mengatur logika terkait dengan admin, seperti manajemen User, manajemen laporan, manajemen tugas, dan operasi administratif lainnya.
   - anggota controller: Mengelola operasi terkait anggota, seperti pendaftaran anggota, menampilkan tugas, konfirmasi tugas, dan aktivitas lainnya.
   - auth controller: Menangani proses otentikasi dan ototorisasi baik user maupun admin untuk akses ke bagian-bagian tertentu pada program.
   - linkedlist controller: Mengatur operasi yang terkait dengan struktur data linked list, seperti penambahan, penghapusan, dan manipulasi data lain pada linked list.
   - user controller: Bertanggung jawab untuk interaksi antara pengguna dengan program, termasuk proses input data seperti laporan dan mengecek laporan, dan hal lain.

3. Folder Model:
   - database: Berisi definisi struktur database dan koneksi ke basis data agar terhubung ke database, dalam hal ini MySQL.

4. Folder View:
   - admin view: Menampilkan antarmuka untuk admin, termasuk menu admin seperti laporan, tugas, user, CRUD admin, dan lain lain.
   - anggota view: Berisi tampilan yang ditujukan untuk anggota, seperti tampilkan tugas, konfirmasi tugas, dan lain-lain.
   - main view: Merupakan tampilan utama yang menampilkan berbagai menu yang muncul diawal pada saat program pertama kali dijalankan, seperti login, daftar, dan lain-lain.
   - user view: Menampilkan antarmuka untuk user, termasuk buat laporan, cek laporan dan lain-lain. 

5. File main.py: Merupakan file utama yang menghubungkan komponen-komponen MVC sehingga menghubungkan antara model, view, dan controller.
C. Fitur dan Fungsionalitas

D. Cara Penggunaan
