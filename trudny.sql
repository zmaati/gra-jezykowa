-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 24 Paź 2023, 09:11
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
-- Struktura tabeli dla tabeli `trudny`
--

CREATE TABLE `trudny` (
  `id` int(11) NOT NULL,
  `pl` text NOT NULL,
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `trudny`
--

INSERT INTO `trudny` (`id`, `pl`, `odp`) VALUES
(1, 'potwór', 'monster'),
(2, 'samochód', 'car'),
(3, 'życie', 'life'),
(4, 'komputer', 'computer'),
(5, 'tramwaj', 'tram'),
(6, 'ulica', 'street'),
(7, 'buty', 'shoes'),
(8, 'siłownia', 'gym'),
(9, 'woda', 'water'),
(10, 'białko', 'protein'),
(11, 'winda', 'elevator'),
(12, 'płot', 'fence'),
(13, 'dach', 'roof'),
(14, 'ściana', 'wall'),
(15, 'okno', 'window'),
(16, 'lewo', 'left'),
(17, 'światło', 'light'),
(18, 'zadanie', 'assignment'),
(19, 'kino', 'cinema'),
(20, 'biblioteka', 'library');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `trudny`
--
ALTER TABLE `trudny`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `trudny`
--
ALTER TABLE `trudny`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
