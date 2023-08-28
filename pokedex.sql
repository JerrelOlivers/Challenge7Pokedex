-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2023 at 02:26 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pokedex`
--

-- --------------------------------------------------------

--
-- Table structure for table `pokemon`
--

CREATE TABLE `pokemon` (
  `id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Attack` varchar(255) NOT NULL,
  `Special` varchar(255) NOT NULL,
  `Defense` varchar(10) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `Type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pokemon`
--

INSERT INTO `pokemon` (`id`, `Name`, `Attack`, `Special`, `Defense`, `Gender`, `Type`) VALUES
(1, 'Bulbasaur', '49', '65', '49', 'Male', 'Grass/Poison'),
(2, 'Ivysaur', '62', '80', '63', 'Male', 'Grass/Poison'),
(3, 'Venusaur', '82', '100', '83', 'Male', 'Grass/Poison'),
(4, 'Charmander', '52', '60', '43', 'Male', 'Fire'),
(5, 'Charmeleon', '64', '80', '58', 'Male', 'Fire'),
(6, 'Charizard', '84', '109', '78', 'Male', 'Fire/Flying'),
(7, 'Squirtle', '48', '50', '65', 'Male', 'Water'),
(8, 'Wartortle', '63', '65', '80', 'Male', 'Water'),
(9, 'Blastoise', '83', '85', '100', 'Male', 'Water'),
(10, 'Caterpie', '30', '20', '35', 'Male', 'Bug'),
(11, 'Metapod', '20', '25', '55', 'Male', 'Bug'),
(12, 'Butterfree', '45', '80', '50', 'Male', 'Bug/Flying'),
(151, 'Mew', '100', '100', '100', 'Gender', 'Psychic');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pokemon`
--
ALTER TABLE `pokemon`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pokemon`
--
ALTER TABLE `pokemon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=152;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
