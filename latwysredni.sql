-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Paź 24, 2023 at 08:33 AM
-- Wersja serwera: 10.4.28-MariaDB
-- Wersja PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `duolingo`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `latwy`
--

CREATE TABLE `latwy` (
  `id` int(11) NOT NULL,
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `latwy`
--

INSERT INTO `latwy` (`id`, `odp`) VALUES
(1, 'apple'),
(2, 'cabbage'),
(3, 'mouse'),
(4, 'tree'),
(5, 'pencil case'),
(6, 'smartphone'),
(7, 'shelf'),
(8, 'painting'),
(9, 'angry'),
(10, 'green'),
(11, 'arm'),
(12, 'armchair'),
(13, 'desktop computer'),
(14, 'shoes'),
(15, 'beer'),
(16, 'eye'),
(17, 'strawberry'),
(18, 'stick'),
(19, 'rain'),
(20, 'mushroom');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `sredni`
--

CREATE TABLE `sredni` (
  `id` int(11) NOT NULL,
  `polski` text NOT NULL,
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sredni`
--

INSERT INTO `sredni` (`id`, `polski`, `odp`) VALUES
(1, 'hulajnoga', 'scooter'),
(2, 'silnik', 'engine'),
(3, 'deszcz', 'rain'),
(4, 'pochmurno', 'cloudy'),
(5, 'lew', 'lion'),
(6, 'samochód', 'car'),
(7, 'wyświetlacz', 'screen'),
(8, 'brzoskwinia', 'peach'),
(9, 'drzewo', 'tree'),
(10, 'buty', 'shoes'),
(11, 'ogród', 'garden'),
(12, 'łąka', 'meadow'),
(13, 'lampa', 'lamp'),
(14, 'aplikacja', 'app'),
(15, 'koty', 'cats'),
(16, 'most', 'bridge'),
(17, 'kolumna', 'column'),
(18, 'ptaki', 'birds'),
(19, 'flowers', 'kwiaty'),
(20, 'kwiat', 'flower');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `latwy`
--
ALTER TABLE `latwy`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `sredni`
--
ALTER TABLE `sredni`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `latwy`
--
ALTER TABLE `latwy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `sredni`
--
ALTER TABLE `sredni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
