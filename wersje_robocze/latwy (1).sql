-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 18 Paź 2023, 11:55
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
  `obrazek` text NOT NULL,
  `odp_a` text NOT NULL,
  `odp_b` text NOT NULL,
  `odp_c` text NOT NULL,
  `odp_d` text NOT NULL,
  `odp_e` text NOT NULL,
  `odp_f` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `latwy`
--

INSERT INTO `latwy` (`id`, `obrazek`, `odp_a`, `odp_b`, `odp_c`, `odp_d`, `odp_e`, `odp_f`) VALUES
(1, 'apple', 'grape', 'apple', 'banana', 'seed', 'cabbage', 'dragonfruit'),
(2, 'cabbage', 'salad', 'lemon', 'orange', 'cabbage', 'cable', 'candy'),
(3, 'mouse', 'keyboard', 'rat', 'strawberry', 'cat', 'dog', 'mouse'),
(4, 'tree', 'tree', 'pear', 'seed', 'bush', 'leaves', 'flower'),
(5, 'pencil case', 'ruler', 'pencil', 'pencil case', 'pen', 'eraser', 'sandwich'),
(6, 'smartphone', 'keyboard', 'smartphone', 'app', 'shoe', 'laptop', 'cable'),
(7, 'shelf', 'shelf', 'dresser', 'bookcase', 'book', 'paper', 'pencil'),
(8, 'painting', 'museum', 'frame', 'painting', 'art', 'pencil', 'brush'),
(9, 'angry', 'sad', 'angry', 'happy', 'stressed', 'emotions', 'crying'),
(10, 'green', 'red', 'blue', 'yellow', 'green', 'blue', 'purple'),
(11, 'arm', 'leg', 'hrad', 'arm', 'hair', 'eye', 'nose'),
(12, 'armchair', 'chair', 'stool', 'table', 'armchair', 'lamp', 'desk'),
(13, 'desktop computer', 'desktop copmuter', 'laptop', 'phone', 'screen', 'keyboard', 'pendrive');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `latwy`
--
ALTER TABLE `latwy`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `latwy`
--
ALTER TABLE `latwy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
