-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 24 Paź 2023, 07:53
-- Wersja serwera: 10.4.25-MariaDB
-- Wersja PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `duolingo`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `latwy`
--

CREATE TABLE `latwy` (
  `id` int(11) NOT NULL,
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `latwy`
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
  `odp_a` text NOT NULL,
  `odp_b` text NOT NULL,
  `odp_c` text NOT NULL,
  `odp_d` text NOT NULL,
  `odp_e` text NOT NULL,
  `odp_f` text NOT NULL,
  `odp_g` text NOT NULL,
  `odp_h` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `sredni`
--

INSERT INTO `sredni` (`id`, `polski`, `odp_a`, `odp_b`, `odp_c`, `odp_d`, `odp_e`, `odp_f`, `odp_g`, `odp_h`) VALUES
(1, 'samochód', 'car', 'scooter', 'motorbike', 'dirtbike', 'van', 'jetskii', 'airplane', 'wheel'),
(2, 'szkoła', 'town', 'roof', 'school', 'building', 'city', 'street', 'shopping mall', 'shop'),
(3, 'kurtka', 'shirt', 'suit', 'jacket', 'hat', 'scarf', 'gloves', 'mask', 'balaclava'),
(4, 'telewizor', 'computer', 'laptop', 'screen', 'desk', 'keyboard', 'TV', 'mouse', 'camera'),
(5, 'salon', 'bedroom', 'hall', 'living room', 'kitchen', 'dining room', 'corridor', 'pendrive', 'house'),
(6, 'czołówka', 'lamp', 'torch', 'flashlight', 'lantern', 'light', 'relfector', 'fire', 'sun');

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
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `latwy`
--
ALTER TABLE `latwy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT dla tabeli `sredni`
--
ALTER TABLE `sredni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
