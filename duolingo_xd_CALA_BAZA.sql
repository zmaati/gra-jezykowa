-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 30 Paź 2023, 20:15
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.2.0

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `sredni`
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

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `srednio_trudny`
--

CREATE TABLE `srednio_trudny` (
  `id` int(11) NOT NULL,
  `pl` text NOT NULL,
  `text` text NOT NULL,
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `srednio_trudny`
--

INSERT INTO `srednio_trudny` (`id`, `pl`, `text`, `odp`) VALUES
(1, 'węgiel', 'c__l', 'o#a'),
(2, 'pszczoła', 'b__', 'e'),
(3, 'frytki', 'fr__s', 'i#e'),
(4, 'osoba', 'p_rs_n', 'e#o'),
(5, 'budynek', 'b__ld_ng', 'u#i'),
(6, 'smród', 'sm_ll', 'e'),
(7, 'gumka', 'r_bb_r', 'u#e'),
(8, 'język', 'l_ng__g_', 'a#u#e'),
(9, 'lotnisko', '__rp_rt', 'a#i#o'),
(10, 'pociąg', 'tr__n', 'a#i'),
(11, 'uprawnienie', 'p_rm_ss__n', 'e#i#o'),
(12, 'książka', 'b__k', 'o'),
(13, 'wiśnia', 'ch_rr_', 'e#y'),
(14, 'zdjęcie', 'ph_t_', 'o'),
(15, 'sok', 'j__c_', 'u#i#e'),
(16, 'ziemniak', 'p_t_t_', 'o#a'),
(17, 'przyjaciel', 'fr__nd', 'i#e'),
(18, 'płatność', 'p__m_nt', 'a#y#e'),
(19, 'pieniądze', 'm_n__', 'o#e#y'),
(20, 'tłumacz', 'tr_nsl_t_r', 'a#o'),
(21, 'język', 't_ng__', 'o#u#e');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `trudny`
--

CREATE TABLE `trudny` (
  `id` int(11) NOT NULL,
  `pl` text NOT NULL,
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- Indeksy dla tabeli `srednio_trudny`
--
ALTER TABLE `srednio_trudny`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `trudny`
--
ALTER TABLE `trudny`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT dla tabeli `srednio_trudny`
--
ALTER TABLE `srednio_trudny`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT dla tabeli `trudny`
--
ALTER TABLE `trudny`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
