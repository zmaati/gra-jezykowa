-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 25 Paź 2023, 12:25
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
-- Struktura tabeli dla tabeli `srednio_trudny`
--

CREATE TABLE `srednio_trudny` (
  `id` int(11) NOT NULL,
  `pl` text NOT NULL,
  `text` text NOT NULL,
  `odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(20, 'tłumacz', 'tr_nsl_t_r', 'a#o');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `srednio_trudny`
--
ALTER TABLE `srednio_trudny`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `srednio_trudny`
--
ALTER TABLE `srednio_trudny`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
