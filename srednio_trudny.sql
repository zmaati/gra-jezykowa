-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 24 Paź 2023, 08:13
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
(1, 'węgiel', 'w_g__l', 'coal'),
(2, 'pszczoła', 'b__', 'bee'),
(3, 'frytki', 'fr__s', 'fries'),
(4, 'osoba', 'p_rs_n', 'person'),
(5, 'budynek', 'b__ld_ng', 'building'),
(6, 'smród', 'sm_ll', 'smell'),
(7, 'gumka', 'r_bb_r', 'rubber'),
(8, 'język', 'l_ng__g_', 'language'),
(9, 'lotnisko', '__rp_r_', 'airport'),
(10, 'pociąg', 'tr__n', 'train'),
(11, 'uprawnienie', 'p_rm_ss__n', 'permission'),
(12, 'książka', 'b__k', 'book'),
(13, 'wiśnia', 'ch_rr_', 'cherry'),
(14, 'zdjęcie', 'ph_t_', 'photo'),
(15, 'sok', 'j__c_', 'juice'),
(16, 'ziemniak', 'p_t_t_', 'potato'),
(17, 'przyjaciel', 'fr__nd', 'friend'),
(18, 'płatność', 'p__m_nt', 'payment'),
(19, 'pieniądze', 'm_n__', 'money'),
(20, 'tłumacz', 'tr_nsl_t_r', 'translator');

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
