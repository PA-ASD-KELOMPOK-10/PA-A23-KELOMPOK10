-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2024 at 02:16 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `customer_service`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID_Admin` int(11) NOT NULL,
  `Nama_Admin` varchar(255) NOT NULL,
  `Password_Admin` varchar(255) NOT NULL,
  `No_HP_Admin` varchar(20) NOT NULL,
  `ID_Laporan` int(11) DEFAULT NULL,
  `email_admin` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ID_Admin`, `Nama_Admin`, `Password_Admin`, `No_HP_Admin`, `ID_Laporan`, `email_admin`) VALUES
(5, 'Arey', 'arey123', '081234567801', NULL, 'arey@gmail.com'),
(6, 'Arya', 'arya123', '081234567802', 42, 'arya@gmail.com'),
(7, 'Alfian', 'alfian123', '081234567803', 43, 'alfian@gmail.com'),
(8, 'Nurul', 'nurul123', '081234567804', 44, 'nurul@gmail.com'),
(9, 'Arey', 'arey123', '081234567801', 45, 'arey@gmail.com'),
(10, 'Arya', 'arya123', '081234567802', 46, 'arya@gmail.com'),
(11, 'Alfian', 'alfian123', '081234567803', 47, 'alfian@gmail.com'),
(12, 'Nurul', 'nurul123', '081234567804', 48, 'nurul@gmail.com'),
(13, 'Arey', 'arey123', '081234567801', 49, 'arey@gmail.com'),
(14, 'Arya', 'arya123', '081234567802', 50, 'arya@gmail.com'),
(15, 'Alfian', 'alfian123', '081234567803', 51, 'alfian@gmail.com'),
(16, 'Nurul', 'nurul123', '081234567804', 52, 'nurul@gmail.com'),
(17, 'Arey', 'arey123', '081234567801', 53, 'arey@gmail.com'),
(18, 'Arya', 'arya123', '081234567802', 54, 'arya@gmail.com'),
(19, 'Alfian', 'alfian123', '081234567803', 55, 'alfian@gmail.com'),
(20, 'Nurul', 'nurul123', '081234567804', 56, 'nurul@gmail.com'),
(21, 'Arey', 'arey123', '081234567801', 57, 'arey@gmail.com'),
(22, 'Arya', 'arya123', '081234567802', 58, 'arya@gmail.com'),
(23, 'Alfian', 'alfian123', '081234567803', 59, 'alfian@gmail.com'),
(24, 'Nurul', 'nurul123', '081234567804', 60, 'nurul@gmail.com'),
(25, 'Arey', 'arey123', '081234567801', 61, 'arey@gmail.com'),
(26, 'Arya', 'arya123', '081234567802', 62, 'arya@gmail.com'),
(27, 'Alfian', 'alfian123', '081234567803', 63, 'alfian@gmail.com'),
(28, 'Nurul', 'nurul123', '081234567804', 64, 'nurul@gmail.com'),
(29, 'Arey', 'arey123', '081234567801', 65, 'arey@gmail.com'),
(30, 'Arya', 'arya123', '081234567802', 66, 'arya@gmail.com'),
(31, 'Alfian', 'alfian123', '081234567803', 67, 'alfian@gmail.com'),
(32, 'Nurul', 'nurul123', '081234567804', 68, 'nurul@gmail.com'),
(33, 'Arey', 'arey123', '081234567801', 69, 'arey@gmail.com'),
(34, 'Arya', 'arya123', '081234567802', 70, 'arya@gmail.com'),
(35, 'Alfian', 'alfian123', '081234567803', 71, 'alfian@gmail.com'),
(36, 'Nurul', 'nurul123', '081234567804', 72, 'nurul@gmail.com'),
(37, 'Arey', 'arey123', '081234567801', 73, 'arey@gmail.com'),
(38, 'Arya', 'arya123', '081234567802', 74, 'arya@gmail.com'),
(39, 'Alfian', 'alfian123', '081234567803', 75, 'alfian@gmail.com'),
(40, 'Nurul', 'nurul123', '081234567804', 76, 'nurul@gmail.com'),
(41, 'Arey', 'arey123', '081234567801', 77, 'arey@gmail.com'),
(42, 'Arya', 'arya123', '081234567802', 78, 'arya@gmail.com'),
(43, 'Alfian', 'alfian123', '081234567803', 79, 'alfian@gmail.com'),
(44, 'Nurul', 'nurul123', '081234567804', 80, 'nurul@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `ID_Anggota` int(11) NOT NULL,
  `Nama_Anggota` varchar(100) NOT NULL,
  `Rangking_Anggota` int(11) NOT NULL,
  `Keahlian_Anggota` varchar(100) NOT NULL,
  `password_anggota` varchar(255) DEFAULT NULL,
  `email_anggota` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`ID_Anggota`, `Nama_Anggota`, `Rangking_Anggota`, `Keahlian_Anggota`, `password_anggota`, `email_anggota`) VALUES
(119, 'Agus Santoso', 1, 'Perbaikan Jalan', 'agus123', 'agussantoso@gmail.com'),
(120, 'Budi Prasetyo', 2, 'Genangan Air', 'budi123', 'budiprasetyo@gmail.com'),
(121, 'Cahyo Nugroho', 3, 'Kerusakan Trotoar', 'cahyo123', 'cahyonugroho@gmail.com'),
(122, 'Dodi Santoso', 4, 'Pohon Tumbang', 'dodi123', 'dodisantoso@gmail.com'),
(123, 'Edi Kurniawan', 5, 'Tiang Listrik Miring', 'edi123', 'edikurniawan@gmail.com'),
(124, 'Firman Maulana', 6, 'Saluran Air Tersumbat', 'firman123', 'firmanmaulana@gmail.com'),
(125, 'Gatot Widodo', 7, 'Kebocoran Pipa', 'gatot123', 'gatotwidodo@gmail.com'),
(126, 'Hadi Sutrisno', 8, 'Bangunan Terbengkalai', 'hadi123', 'hadisutrisno@gmail.com'),
(127, 'Irfan Wahyudi', 9, 'Kerusakan Jalan Berlubang', 'irfan123', 'irfanwahyudi@gmail.com'),
(128, 'Joko Susanto', 10, 'Kerusakan Jalan', 'joko123', 'jokosusanto@gmail.com'),
(129, 'Kurniawan Wijaya', 11, 'Kerukasan Jalan', 'kurniawan123', 'kurniawanwijaya@gmail.com'),
(130, 'Lukman Hakim', 12, 'Genangan Air', 'lukman123', 'lukmanhakim@gmail.com'),
(131, 'Maman Sulaeman', 13, 'Kebocoran Pipa Gas', 'maman123', 'mamansulaeman@gmail.com'),
(132, 'Nurhadi Pratama', 14, 'Tiang Listrik Miring', 'nurhadi123', 'nurhadipratama@gmail.com'),
(133, 'Oky Setiawan', 15, 'Saluran Air Tersumbat', 'oky123', 'okysetiawan@gmail.com'),
(134, 'Prabowo Wibowo', 16, 'Bangunan Terbengkalai', 'prabowo123', 'prabowowibowo@gmail.com'),
(135, 'Qori Ramadhan', 17, 'Kerusakan Jalan Berlubang', 'qori123', 'qoriramadhan@gmail.com'),
(136, 'Rudi Susilo', 18, 'Kerusakan Trotoar', 'rudi123', 'rudisusilo@gmail.com'),
(137, 'Samsul Arifin', 19, 'Kerusakan Jalan', 'samsul123', 'samsularifin@gmail.com'),
(138, 'Taufik Hidayat', 20, 'Pohon Tumbang', 'taufik123', 'taufikhidayat@gmail.com'),
(139, 'Umar Faruq', 21, 'Tiang Listrik Miring', 'umar123', 'umarfaruq@gmail.com'),
(140, 'Viki Pratama', 22, 'Kebocoran Pipa Gas', 'viki123', 'vikipratama@gmail.com'),
(141, 'Wawan Sutisna', 23, 'Genangan Air', 'wawan123', 'wawansutisna@gmail.com'),
(142, 'Xavier Budiman', 24, 'Pohon Tumbang', 'xavier123', 'xavierbudiman@gmail.com'),
(143, 'Yoga Pratama', 25, 'Bangunan Terbengkalai', 'yoga123', 'yogapratama@gmail.com'),
(144, 'Zainal Abidin', 26, 'Kerusakan Jalan Berlubang', 'zainal123', 'zainalabidin@gmail.com'),
(145, 'Andi Kusuma', 27, 'Kerusakan Trotoar', 'andi123', 'andikusuma@gmail.com'),
(146, 'Bambang Santoso', 28, 'Saluran Air Tersumbat', 'bambang123', 'bambangsantoso@gmail.com'),
(147, 'Candra Wijaya', 29, 'Tiang Listrik Miring', 'candra123', 'candrawijaya@gmail.com'),
(148, 'Dedi Priyanto', 30, 'Kebocoran Pipa', 'dedi123', 'dedipriyanto@gmail.com'),
(149, 'Eko Nugroho', 31, 'Pohon Tumbang', 'eko123', 'ekonugroho@gmail.com'),
(150, 'Fandi Maulana', 32, 'Genangan Air', 'fandi123', 'fandimaulana@gmail.com'),
(151, 'Gatot Subroto', 33, 'Kebocoran Pipa Gas', 'gatot123', 'gatotsubroto@gmail.com'),
(152, 'Hari Wibowo', 34, 'Tiang Listrik Miring', 'hari123', 'hariwibowo@gmail.com'),
(153, 'Indra Gunawan', 35, 'Saluran Air Tersumbat', 'indra123', 'indragunawan@gmail.com'),
(154, 'Joko Santoso', 36, 'Bangunan Terbengkalai', 'joko123', 'jokosantoso@gmail.com'),
(155, 'Kusnadi Wijaya', 37, 'Kerusakan Jalan Berlubang', 'kusnadi123', 'kusnadiwijaya@gmail.com'),
(156, 'Lukman Hakim', 38, 'Kerusakan Trotoar', 'lukman123', 'lukmanhakim@gmail.com'),
(157, 'Muhammad Taufik', 39, 'Pohon Tumbang', 'muhammad123', 'muhammadtaufik@gmail.com'),
(158, 'Nanang Supriatna', 40, 'Tiang Listrik Miring', 'nanang123', 'nanangsupriatna@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `laporan`
--

CREATE TABLE `laporan` (
  `ID_Laporan` int(11) NOT NULL,
  `ID_User` int(11) NOT NULL,
  `Isi_Laporan` varchar(500) NOT NULL,
  `Lokasi_Laporan` varchar(100) NOT NULL,
  `status_laporan` varchar(255) NOT NULL DEFAULT 'pending',
  `respon_admin` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laporan`
--

INSERT INTO `laporan` (`ID_Laporan`, `ID_User`, `Isi_Laporan`, `Lokasi_Laporan`, `status_laporan`, `respon_admin`) VALUES
(42, 42, 'Terdapat genangan air di sekitar area parkir kompleks perumahan Citra Garden Samarinda, menyulitkan penghuni untuk parkir.', 'Area Parkir Kompleks Perumahan Citra Garden, Samarinda', 'pending', NULL),
(43, 43, 'Kerusakan jalan berlubang di Jalan Manggis Samarinda membuat pengguna jalan sering terjatuh.', 'Jalan Manggis, Samarinda', 'pending', NULL),
(44, 44, 'Pohon tumbang menimpa pagar di depan kompleks perumahan Bumi Sejahtera Samarinda, merusak properti penghuni.', 'Kompleks Perumahan Bumi Sejahtera, Samarinda', 'pending', NULL),
(45, 45, 'Terjadi kebocoran pipa air di dekat taman kota Samarinda, menyebabkan genangan air di area taman.', 'Dekat Taman Kota, Samarinda', 'pending', NULL),
(46, 46, 'Tiang listrik miring di dekat pusat perbelanjaan Samarinda Plaza, mengancam keselamatan pengunjung.', 'Dekat Samarinda Plaza', 'pending', NULL),
(47, 47, 'Saluran air di sepanjang Jalan Rambutan Samarinda tersumbat, menyebabkan banjir saat hujan deras.', 'Jalan Rambutan, Samarinda', 'pending', NULL),
(48, 48, 'Pohon besar tumbang menutupi jalan dekat kompleks perumahan Bumi Indah Samarinda, menghambat akses kendaraan.', 'Kompleks Perumahan Bumi Indah, Samarinda', 'pending', NULL),
(49, 49, 'Kerusakan jalan di depan gereja Katedral Samarinda membuat pengguna jalan kesulitan melintas.', 'Depan Gereja Katedral Samarinda', 'pending', NULL),
(50, 50, 'Terjadi kebocoran pipa gas di sekitar area industri Samarinda Seberang, meningkatkan risiko kebakaran.', 'Area Industri Samarinda Seberang', 'pending', NULL),
(51, 51, 'Bangunan kosong di depan kompleks perumahan Mutiara Baru Samarinda menjadi tempat berkumpulnya preman, membahayakan keamanan warga.', 'Depan Kompleks Perumahan Mutiara Baru, Samarinda', 'pending', NULL),
(52, 52, 'Trotoar di depan sekolah SMP Negeri 2 Samarinda Barat rusak parah, mengganggu akses pejalan kaki.', 'Sekolah SMP Negeri 2 Samarinda Barat', 'pending', NULL),
(53, 53, 'Terdapat genangan air di depan kompleks perumahan Permata Hijau Samarinda, menyulitkan akses keluar masuk penghuni.', 'Kompleks Perumahan Permata Hijau, Samarinda', 'pending', NULL),
(54, 54, 'Kerusakan jalan berlubang di Jalan Mawar Samarinda membuat kendaraan sering terperosok.', 'Jalan Mawar, Samarinda', 'pending', NULL),
(55, 55, 'Tiang listrik miring di dekat lapangan sepak bola Samarinda membuat risiko tersengat listrik bagi pemain.', 'Dekat Lapangan Sepak Bola Samarinda', 'pending', NULL),
(56, 56, 'Saluran air di dekat jalan raya Samarinda-Balikpapan tersumbat, menyebabkan banjir saat hujan deras.', 'Jalan Raya Samarinda-Balikpapan', 'pending', NULL),
(57, 57, 'Terdapat pohon besar tumbang menutupi jalan di kompleks perumahan Taman Harapan Samarinda, mengganggu arus lalu lintas.', 'Kompleks Perumahan Taman Harapan, Samarinda', 'pending', NULL),
(58, 58, 'Kebocoran pipa air di dekat area parkir Mal Pelayanan Publik Samarinda menyebabkan genangan air di sekitar area parkir.', 'Dekat Area Parkir Mal Pelayanan Publik Samarinda', 'pending', NULL),
(59, 59, 'Terjadi tumpahan minyak di dekat pelabuhan Sungai Kunjang Samarinda, mengancam lingkungan hidup di sekitar.', 'Dekat Pelabuhan Sungai Kunjang, Samarinda', 'pending', NULL),
(60, 60, 'Bangunan kosong di dekat kompleks perumahan Permata Bumi Samarinda menjadi tempat berkumpulnya pengemis dan gelandangan.', 'Depan Kompleks Perumahan Permata Bumi, Samarinda', 'pending', NULL),
(61, 61, 'Trotoar di depan pusat perbelanjaan Samarinda Trade Center rusak parah, menyulitkan pejalan kaki.', 'Depan Samarinda Trade Center', 'diterima', 'Laporan Anda mengenai trotoar rusak di depan pusat perbelanjaan Samarinda Trade Center telah diterima. Kami akan segera mengirim tim untuk melakukan perbaikan. Pastikan untuk berhati-hati saat melewati area tersebut.'),
(62, 62, 'Terdapat genangan air di dekat terminal bus Antar Kota Samarinda, mengganggu akses ke terminal.', 'Dekat Terminal Bus Antar Kota Samarinda', 'diterima', 'Kami akan menindaklanjuti laporan Anda mengenai genangan air di dekat terminal bus Antar Kota Samarinda. Salah satu langkah yang dapat kami lakukan adalah membersihkan saluran air untuk memperlancar aliran air.'),
(63, 63, 'Kerusakan jalan berlubang di Jalan S. Parman Samarinda membuat pengguna jalan sering terjatuh.', 'Jalan S. Parman, Samarinda', 'diterima', 'Respon Anda diterima. Kami akan segera memperbaiki kerusakan jalan berlubang di Jalan S. Parman, Samarinda, untuk meningkatkan keselamatan pengguna jalan.'),
(64, 64, 'Tiang listrik miring di dekat jalan raya Samarinda-Bontang mengancam keselamatan pengguna jalan.', 'Dekat Jalan Raya Samarinda-Bontang', 'diterima', 'Kami akan menangani tiang listrik miring di dekat jalan raya Samarinda-Bontang untuk menghindari risiko keselamatan pengguna jalan.'),
(65, 65, 'Saluran air di sepanjang Jalan Danau Sentarum Samarinda tersumbat, menyebabkan banjir saat hujan deras.', 'Jalan Danau Sentarum, Samarinda', 'diterima', 'Pesan Anda diterima. Kami akan membersihkan saluran air di sepanjang Jalan Danau Sentarum, Samarinda, untuk mencegah banjir saat hujan deras.'),
(66, 66, 'Terdapat pohon besar tumbang menimpa pagar di kompleks perumahan Puri Beringin Samarinda, merusak properti penghuni.', 'Kompleks Perumahan Puri Beringin, Samarinda', 'diterima', 'Kami akan segera mengirim tim untuk membersihkan pohon besar tumbang di kompleks perumahan Puri Beringin, Samarinda, yang telah Anda laporkan.'),
(67, 67, 'Kebocoran pipa air di dekat kawasan industri Samarinda Utara meningkatkan risiko pencemaran lingkungan.', 'Dekat Kawasan Industri Samarinda Utara', 'diterima', 'Terima kasih atas laporannya. Kami akan menindaklanjuti kebocoran pipa air di dekat kawasan industri Samarinda Utara untuk mengurangi risiko pencemaran lingkungan.'),
(68, 68, 'Terjadi tumpahan limbah kimia di dekat sungai di wilayah perkampungan Sungai Pinang Samarinda, mengancam kesehatan warga.', 'Dekat Sungai Pinang, Samarinda', 'diterima', 'Kami akan memeriksa tumpahan limbah kimia di sekitar Sungai Pinang, Samarinda, untuk mencegah ancaman terhadap kesehatan warga.'),
(69, 69, 'Bangunan kosong di dekat jalan raya Samarinda-Balikpapan menjadi sarang pengemis dan gelandangan, mengganggu keamanan pengguna jalan.', 'Dekat Jalan Raya Samarinda-Balikpapan', 'diterima', 'Respon Anda diterima. Kami akan menangani bangunan kosong di dekat jalan raya Samarinda-Balikpapan untuk meningkatkan keamanan pengguna jalan.'),
(70, 70, 'Trotoar di depan kompleks perumahan Graha Kencana Samarinda rusak parah, menyulitkan akses pejalan kaki.', 'Kompleks Perumahan Graha Kencana, Samarinda', 'diterima', 'Pesan diterima. Kami akan segera memperbaiki trotoar rusak di depan kompleks perumahan Graha Kencana, Samarinda.'),
(71, 71, 'Terdapat genangan air di depan kantor pemerintahan Provinsi Kalimantan Timur Samarinda, mengganggu aktivitas pemerintahan.', 'Depan Kantor Pemerintahan Provinsi Kalimantan Timur, Samarinda', 'diterima', 'Kami akan menangani genangan air di depan kantor pemerintahan Provinsi Kalimantan Timur Samarinda untuk memastikan kelancaran aktivitas pemerintahan.'),
(72, 72, 'Kerusakan jalan berlubang di Jalan Iskandar Muda Samarinda membuat pengguna jalan sering terjatuh.', 'Jalan Iskandar Muda, Samarinda', 'diterima', 'Laporan Anda diterima. Kami akan segera memperbaiki kerusakan jalan berlubang di Jalan Iskandar Muda, Samarinda.'),
(73, 73, 'Tiang listrik miring di dekat area pemukiman padat penduduk Samarinda Seberang mengancam keselamatan warga.', 'Dekat Samarinda Seberang', 'diterima', 'Terima kasih atas laporannya. Kami akan menindaklanjuti tiang listrik miring di dekat pemukiman padat penduduk Samarinda Seberang untuk meningkatkan keselamatan warga.'),
(74, 74, 'Saluran air di sepanjang Jalan S. Parman Samarinda tersumbat, menyebabkan banjir saat hujan deras.', 'Jalan S. Parman, Samarinda', 'diterima', 'Kami akan membersihkan saluran air di sepanjang Jalan S. Parman, Samarinda, untuk mencegah banjir saat hujan deras.'),
(75, 75, 'Terdapat pohon besar tumbang menimpa rumah di wilayah perkampungan Sungai Kunjang Samarinda, merusak properti warga.', 'Perkampungan Sungai Kunjang, Samarinda', 'diterima', 'Pesan diterima. Kami akan segera mengirim tim untuk membersihkan pohon besar tumbang di perkampungan Sungai Kunjang, Samarinda.'),
(76, 76, 'Kebocoran pipa air di dekat sekolah SDN 3 Samarinda Barat membuat genangan air di halaman sekolah.', 'Sekolah SDN 3 Samarinda Barat', 'diterima', 'Respon Anda diterima. Kami akan menangani kebocoran pipa air di dekat sekolah SDN 3 Samarinda Barat untuk menjaga keamanan siswa dan lingkungan sekolah.'),
(77, 77, 'Terjadi kebocoran pipa gas di dekat pusat perbelanjaan Hypermart Samarinda, meningkatkan risiko kebakaran.', 'Dekat Hypermart Samarinda', 'diterima', 'Terima kasih atas laporannya. Kami akan menangani kebocoran pipa gas di dekat pusat perbelanjaan Hypermart Samarinda untuk mencegah risiko kebakaran.'),
(78, 78, 'Bangunan kosong di dekat kompleks perumahan Citra Indah Samarinda menjadi tempat berkumpulnya preman, membahayakan keamanan warga.', 'Depan Kompleks Perumahan Citra Indah, Samarinda', 'diterima', 'Kami akan menindaklanjuti bangunan kosong di dekat kompleks perumahan Citra Indah Samarinda untuk meningkatkan keamanan warga.'),
(79, 79, 'Trotoar di depan sekolah SMA Negeri 7 Samarinda rusak parah, mengganggu akses pejalan kaki.', 'Sekolah SMA Negeri 7 Samarinda', 'diterima', 'Laporan Anda diterima. Kami akan segera memperbaiki trotoar rusak di depan sekolah SMA Negeri 7 Samarinda untuk memastikan keselamatan siswa.'),
(80, 80, 'Terdapat genangan air di depan terminal bus Terminal Pahandut Samarinda, menyulitkan akses ke terminal.', 'Depan Terminal Bus Terminal Pahandut, Samarinda', 'diterima', 'Kami akan menangani genangan air di depan terminal bus Terminal Pahandut Samarinda untuk memperlancar akses ke terminal.');

-- --------------------------------------------------------

--
-- Table structure for table `tugas`
--

CREATE TABLE `tugas` (
  `ID_Tugas` int(11) NOT NULL,
  `ID_Admin` int(11) NOT NULL,
  `ID_Anggota` int(11) NOT NULL,
  `Tugas_Laporan` varchar(100) NOT NULL,
  `Lokasi_Laporan` varchar(100) NOT NULL,
  `status_tugas` varchar(50) DEFAULT 'on progress'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tugas`
--

INSERT INTO `tugas` (`ID_Tugas`, `ID_Admin`, `ID_Anggota`, `Tugas_Laporan`, `Lokasi_Laporan`, `status_tugas`) VALUES
(1, 5, 119, 'Lubang jalan dekat sekolah SMP Negeri 3 Samarinda, hati-hati pengendara.', 'Dekat SMP Negeri 3 Samarinda', 'selesai'),
(2, 6, 120, 'Genangan air di area parkir Citra Garden Samarinda, sulit parkir.', 'Area Parkir Citra Garden, Samarinda', 'selesai'),
(3, 7, 121, 'Jalan berlubang di Jalan Manggis Samarinda, sering terjatuh.', 'Jalan Manggis, Samarinda', 'selesai'),
(4, 8, 122, 'Pohon tumbang menimpa pagar di perumahan Bumi Sejahtera Samarinda, rusak properti.', 'Perumahan Bumi Sejahtera, Samarinda', 'selesai'),
(5, 5, 123, 'Kebocoran pipa air dekat taman kota Samarinda, genangan air.', 'Dekat Taman Kota, Samarinda', 'selesai'),
(6, 6, 124, 'Tiang listrik miring di dekat pusat perbelanjaan Samarinda Plaza, bahaya pengunjung.', 'Dekat Samarinda Plaza, Samarinda', 'selesai'),
(7, 7, 125, 'Saluran air tersumbat di Jalan Rambutan Samarinda, banjir saat hujan deras.', 'Jalan Rambutan, Samarinda', 'selesai'),
(8, 8, 126, 'Pohon besar tumbang menutupi jalan dekat perumahan Bumi Indah Samarinda, hambat akses.', 'Perumahan Bumi Indah, Samarinda', 'selesai'),
(11, 7, 129, 'Bangunan kosong depan perumahan Mutiara Baru Samarinda, tempat berkumpul preman.', 'Depan Perumahan Mutiara Baru, Samarinda', 'selesai'),
(12, 8, 130, 'Trotoar di depan sekolah SMP Negeri 2 Samarinda Barat rusak parah, ganggu pejalan kaki.', 'Sekolah SMP Negeri 2 Samarinda Barat', 'selesai'),
(13, 5, 131, 'Genangan air di kompleks perumahan Permata Hijau Samarinda, sulit keluar masuk.', 'Perumahan Permata Hijau, Samarinda', 'selesai'),
(14, 6, 132, 'Jalan berlubang di Jalan Mawar Samarinda, kendaraan sering terperosok.', 'Jalan Mawar, Samarinda', 'selesai'),
(15, 7, 133, 'Tiang listrik miring di dekat lapangan sepak bola Samarinda, risiko tersengat listrik.', 'Dekat Lapangan Sepak Bola Samarinda', 'selesai'),
(16, 8, 134, 'Saluran air di Jalan Raya Samarinda-Balikpapan tersumbat, banjir saat hujan deras.', 'Jalan Raya Samarinda-Balikpapan', 'selesai'),
(17, 5, 135, 'Pohon besar tumbang menutupi jalan di perumahan Taman Harapan Samarinda, ganggu lalu lintas.', 'Perumahan Taman Harapan, Samarinda', 'selesai'),
(18, 6, 136, 'Kebocoran pipa air dekat area parkir Mal Pelayanan Publik Samarinda, genangan air.', 'Dekat Area Parkir Mal Pelayanan Publik Samarinda', 'selesai'),
(19, 7, 137, 'Tumpahan minyak di pelabuhan Sungai Kunjang Samarinda, ancam lingkungan hidup.', 'Dekat Pelabuhan Sungai Kunjang, Samarinda', 'selesai'),
(20, 8, 138, 'Bangunan kosong dekat perumahan Permata Bumi Samarinda, tempat berkumpul pengemis gelandangan.', 'Depan Perumahan Permata Bumi, Samarinda', 'selesai'),
(21, 5, 139, 'Trotoar depan Samarinda Trade Center rusak parah, ganggu pejalan kaki.', 'Depan Samarinda Trade Center', 'on progress'),
(22, 6, 140, 'Genangan air dekat terminal bus Antar Kota Samarinda, sulit akses terminal.', 'Dekat Terminal Bus Antar Kota Samarinda', 'on progress'),
(23, 7, 141, 'Jalan berlubang di Jalan S. Parman Samarinda, pengguna jalan sering terjatuh.', 'Jalan S. Parman, Samarinda', 'on progress'),
(24, 8, 142, 'Tiang listrik miring dekat pemukiman padat penduduk Samarinda Seberang, ancam keselamatan warga.', 'Dekat Samarinda Seberang, Samarinda', 'on progress'),
(25, 5, 143, 'Saluran air di Jalan S. Parman Samarinda tersumbat, banjir saat hujan deras.', 'Jalan S. Parman, Samarinda', 'on progress'),
(26, 6, 144, 'Pohon besar tumbang menimpa rumah di perkampungan Sungai Kunjang Samarinda, rusak properti warga.', 'Perkampungan Sungai Kunjang, Samarinda', 'on progress'),
(27, 7, 145, 'Kebocoran pipa air dekat sekolah SDN 3 Samarinda Barat, genangan air di halaman sekolah.', 'Sekolah SDN 3 Samarinda Barat', 'on progress'),
(28, 8, 146, 'Kebocoran pipa gas dekat pusat perbelanjaan Hypermart Samarinda, risiko kebakaran.', 'Dekat Hypermart Samarinda', 'on progress'),
(29, 5, 147, 'Bangunan kosong dekat perumahan Citra Indah Samarinda, tempat berkumpul preman.', 'Depan Perumahan Citra Indah, Samarinda', 'on progress'),
(30, 6, 148, 'Trotoar depan SMA Negeri 7 Samarinda rusak parah, ganggu akses pejalan kaki.', 'Depan SMA Negeri 7 Samarinda', 'on progress'),
(31, 7, 149, 'Genangan air depan terminal bus Terminal Pahandut Samarinda, sulit akses terminal.', 'Depan Terminal Bus Terminal Pahandut, Samarinda', 'on progress'),
(32, 8, 150, 'Jalan berlubang di Jalan Iskandar Muda Samarinda, pengguna jalan sering terjatuh.', 'Jalan Iskandar Muda, Samarinda', 'on progress'),
(33, 5, 151, 'Tiang listrik miring dekat area pemukiman padat penduduk Samarinda Seberang, ancam keselamatan warga', 'Dekat Samarinda Seberang, Samarinda', 'on progress'),
(34, 6, 152, 'Saluran air di Jalan S. Parman Samarinda tersumbat, banjir saat hujan deras.', 'Jalan S. Parman, Samarinda', 'on progress'),
(35, 7, 153, 'Pohon besar tumbang menimpa rumah di perkampungan Sungai Kunjang Samarinda, rusak properti warga.', 'Perkampungan Sungai Kunjang, Samarinda', 'on progress'),
(36, 8, 154, 'Kebocoran pipa air dekat sekolah SDN 3 Samarinda Barat, genangan air di halaman sekolah.', 'Sekolah SDN 3 Samarinda Barat', 'on progress'),
(37, 5, 155, 'Kebocoran pipa gas dekat pusat perbelanjaan Hypermart Samarinda, risiko kebakaran.', 'Dekat Hypermart Samarinda', 'on progress'),
(38, 6, 156, 'Bangunan kosong dekat perumahan Citra Indah Samarinda, tempat berkumpul preman.', 'Depan Perumahan Citra Indah, Samarinda', 'on progress'),
(39, 7, 157, 'Trotoar depan SMA Negeri 7 Samarinda rusak parah, ganggu akses pejalan kaki.', 'Depan SMA Negeri 7 Samarinda', 'on progress');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `ID_User` int(11) NOT NULL,
  `ID_Admin` int(11) DEFAULT NULL,
  `Nama_User` varchar(255) NOT NULL,
  `Password_User` varchar(255) NOT NULL,
  `Email_User` varchar(100) NOT NULL,
  `Alamat` varchar(100) NOT NULL,
  `No_Hp` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`ID_User`, `ID_Admin`, `Nama_User`, `Password_User`, `Email_User`, `Alamat`, `No_Hp`) VALUES
(41, 5, 'Fadil', 'Fadil123', 'fadil@gmail.com', 'Jalan Pangeran Antasari No. 23, Kel. Mulya Sari, Kec. Samarinda Ulu, Samarinda', '082156897101'),
(42, 6, 'Arini', 'Arini123', 'arini@gmail.com', 'Jalan Cendana No. 45, Kel. Sungai Kunjang, Kec. Sungai Kunjang, Samarinda', '082256987102'),
(43, 7, 'Anita', 'Anita123', 'anita@gmail.com', 'Jalan Kartini No. 27, Kel. Mulya Sari, Kec. Samarinda Ulu, Samarinda', '082356789103'),
(44, 8, 'Septiyani', 'Septiyani123', 'septiyani@gmail.com', 'Jalan Kenangan No. 8, Kel. Teluk Lerong Ilir, Kec. Samarinda Seberang, Samarinda', '082056987104'),
(45, 5, 'Lisa', 'Lisa123', 'lisa@gmail.com', 'Jalan Flamboyan No. 25, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082156987105'),
(46, 6, 'Alya', 'Alya123', 'alya@gmail.com', 'Jalan Melati No. 50, Kel. Sungai Siring, Kec. Samarinda Ilir, Samarinda', '082256789106'),
(47, 7, 'Alyssa', 'Alyssa123', 'alyssa@gmail.com', 'Jalan Teratai No. 13, Kel. Sungai Keledang, Kec. Samarinda Ilir, Samarinda', '082356987107'),
(48, 8, 'Athira', 'Athira123', 'athira@gmail.com', 'Jalan Anggrek No. 30, Kel. Temenggungan, Kec. Sungai Kunjang, Samarinda', '082056789108'),
(49, 5, 'Diva', 'Diva123', 'diva@gmail.com', 'Jalan Mawar No. 55, Kel. Samarinda Seberang, Kec. Samarinda Seberang, Samarinda', '082156987109'),
(50, 6, 'Hana', 'Hana123', 'hana@gmail.com', 'Jalan Kamboja No. 18, Kel. Sungai Siring, Kec. Samarinda Ilir, Samarinda', '082256789110'),
(51, 7, 'Annida', 'Annida123', 'annida@gmail.com', 'Jalan Flamboyan No. 40, Kel. Sempaja Selatan, Kec. Samarinda Ulu, Samarinda', '082356789111'),
(52, 8, 'Aidhil', 'Aidhil123', 'aidhil@gmail.com', 'Jalan Kenari No. 33, Kel. Sungai Siring, Kec. Samarinda Ilir, Samarinda', '082056789112'),
(53, 5, 'Irene', 'Irene123', 'irene@gmail.com', 'Jalan Kencana No. 65, Kel. Sempaja Selatan, Kec. Samarinda Ulu, Samarinda', '082156789113'),
(54, 6, 'Fitri', 'Fitri123', 'fitri@gmail.com', 'Jalan Beringin No. 75, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082256789114'),
(55, 7, 'Nazwa', 'Nazwa123', 'nazwa@gmail.com', 'Jalan Angsana No. 20, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082356789115'),
(56, 8, 'Widia', 'Widia123', 'widia@gmail.com', 'Jalan Salak No. 38, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082056789116'),
(57, 5, 'Hisyam', 'Hisyam123', 'hisyam@gmail.com', 'Jalan Terong No. 55, Kel. Sungai Siring, Kec. Samarinda Ilir, Samarinda', '082156789117'),
(58, 6, 'Fitriani', 'Fitriani123', 'fitriani@gmail.com', 'Jalan Mangga No. 70, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082256789118'),
(59, 7, 'Imam', 'Imam123', 'imam@gmail.com', 'Jalan Durian No. 10, Kel. Sungai Kunjang, Kec. Sungai Kunjang, Samarinda', '082356789119'),
(60, 8, 'Salsabilla', 'Salsabilla123', 'salsabilla@gmail.com', 'Jalan Pisang No. 45, Kel. Sempaja Selatan, Kec. Samarinda Ulu, Samarinda', '082056789120'),
(61, 5, 'Nely', 'Nely123', 'nely@gmail.com', 'Jalan Anggur No. 80, Kel. Temenggungan, Kec. Sungai Kunjang, Samarinda', '082156789121'),
(62, 6, 'Khairu', 'Khairu123', 'khairu@gmail.com', 'Jalan Lengkeng No. 17, Kel. Sungai Siring, Kec. Samarinda Ilir, Samarinda', '082256789122'),
(63, 7, 'Rofi', 'Rofi123', 'rofi@gmail.com', 'Jalan Rambutan No. 29, Kel. Sungai Keledang, Kec. Samarinda Ilir, Samarinda', '082356789123'),
(64, 8, 'Farhan', 'Farhan123', 'farhan@gmail.com', 'Jalan Jeruk No. 7, Kel. Teluk Lerong Ilir, Kec. Samarinda Seberang, Samarinda', '082056789124'),
(65, 5, 'Rofiif', 'Rofiif123', 'rofiif@gmail.com', 'Jalan Manggis No. 11, Kel. Temenggungan, Kec. Sungai Kunjang, Samarinda', '082156789125'),
(66, 6, 'Lintang', 'Lintang123', 'lintang@gmail.com', 'Jalan Nanas No. 36, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082256789126'),
(67, 7, 'Dzaky', 'Dzaky123', 'dzaky@gmail.com', 'Jalan Markisa No. 22, Kel. Sempaja Selatan, Kec. Samarinda Ulu, Samarinda', '082356789127'),
(68, 8, 'Naura', 'Naura123', 'naura@gmail.com', 'Jalan Apel No. 48, Kel. Sungai Keledang, Kec. Samarinda Ilir, Samarinda', '082056789128'),
(69, 5, 'Iqbal', 'Iqbal123', 'iqbal@gmail.com', 'Jalan Sawo No. 14, Kel. Sungai Siring, Kec. Samarinda Ilir, Samarinda', '082156789129'),
(70, 6, 'Nabil', 'Nabil123', 'nabil@gmail.com', 'Jalan Mangga No. 9, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082256789130'),
(71, 7, 'Yasmin', 'Yasmin123', 'yasmin@gmail.com', 'Jalan Jeruk No. 6, Kel. Sempaja Selatan, Kec. Samarinda Ulu, Samarinda', '082356789131'),
(72, 8, 'Dhea', 'Dhea123', 'dhea@gmail.com', 'Jalan Melon No. 42, Kel. Sungai Kunjang, Kec. Sungai Kunjang, Samarinda', '082056789132'),
(73, 5, 'Andromeda', 'Andromeda123', 'andromeda@gmail.com', 'Jalan Alpukat No. 51, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082156789133'),
(74, 6, 'Rizky', 'Rizky123', 'rizky@gmail.com', 'Jalan Manggis No. 88, Kel. Sungai Keledang, Kec. Samarinda Ilir, Samarinda', '082256789134'),
(75, 7, 'Mirza', 'Mirza123', 'mirza@gmail.com', 'Jalan Mangga No. 71, Kel. Sungai Siring, Kec. Samarinda Ilir, Samarinda', '082456789135'),
(76, 8, 'David', 'David123', 'david@gmail.com', 'Jalan Mangga No. 56, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082556789136'),
(77, 5, 'Rifqi', 'Rifqi123', 'rifqi@gmail.com', 'Jalan Nanas No. 39, Kel. Sungai Kunjang, Kec. Sungai Kunjang, Samarinda', '082656789137'),
(78, 6, 'Nova', 'Nova123', 'nova@gmail.com', 'Jalan Nanas No. 10, Kel. Sidodadi, Kec. Samarinda Ulu, Samarinda', '082756789138'),
(79, 7, 'Regar', 'Regar123', 'regar@gmail.com', 'Jalan Nanas No. 55, Kel. Sempaja Selatan, Kec. Samarinda Ulu, Samarinda', '082856789139'),
(80, 8, 'Najla', 'Najla123', 'najla@gmail.com', 'Jalan Nanas No. 80, Kel. Sungai Keledang, Kec. Samarinda Ilir, Samarinda', '082956789140');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID_Admin`),
  ADD KEY `ID_Laporan` (`ID_Laporan`);

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`ID_Anggota`);

--
-- Indexes for table `laporan`
--
ALTER TABLE `laporan`
  ADD PRIMARY KEY (`ID_Laporan`),
  ADD KEY `ID_User` (`ID_User`);

--
-- Indexes for table `tugas`
--
ALTER TABLE `tugas`
  ADD PRIMARY KEY (`ID_Tugas`),
  ADD KEY `ID_Admin` (`ID_Admin`),
  ADD KEY `ID_Anggota` (`ID_Anggota`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID_User`),
  ADD KEY `idx_ID_Admin` (`ID_Admin`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID_Admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `anggota`
--
ALTER TABLE `anggota`
  MODIFY `ID_Anggota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=159;

--
-- AUTO_INCREMENT for table `laporan`
--
ALTER TABLE `laporan`
  MODIFY `ID_Laporan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=91;

--
-- AUTO_INCREMENT for table `tugas`
--
ALTER TABLE `tugas`
  MODIFY `ID_Tugas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `ID_User` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`ID_Laporan`) REFERENCES `laporan` (`ID_Laporan`);

--
-- Constraints for table `laporan`
--
ALTER TABLE `laporan`
  ADD CONSTRAINT `laporan_ibfk_1` FOREIGN KEY (`ID_User`) REFERENCES `user` (`ID_User`);

--
-- Constraints for table `tugas`
--
ALTER TABLE `tugas`
  ADD CONSTRAINT `tugas_ibfk_1` FOREIGN KEY (`ID_Admin`) REFERENCES `admin` (`ID_Admin`),
  ADD CONSTRAINT `tugas_ibfk_2` FOREIGN KEY (`ID_Anggota`) REFERENCES `anggota` (`ID_Anggota`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `FK_ID_Admin` FOREIGN KEY (`ID_Admin`) REFERENCES `admin` (`ID_Admin`),
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`ID_Admin`) REFERENCES `admin` (`ID_Admin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
