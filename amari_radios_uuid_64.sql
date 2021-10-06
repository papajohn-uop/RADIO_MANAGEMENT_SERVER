-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: rc_mysql_cont:3306
-- Generation Time: Oct 06, 2021 at 12:28 PM
-- Server version: 5.7.29
-- PHP Version: 7.4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `radio_config`
--

-- --------------------------------------------------------

--
-- Table structure for table `amari_radios`
--

CREATE TABLE `amari_radios` (
  `id` int(11) NOT NULL,
  `UUID` varchar(64) NOT NULL,
  `name` varchar(256) NOT NULL,
  `description` varchar(256) DEFAULT NULL,
  `resourceVersion` varchar(128) DEFAULT NULL,
  `resource_characteristic` json DEFAULT NULL,
  `placeholder` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `amari_radios`
--

INSERT INTO `amari_radios` (`id`, `UUID`, `name`, `description`, `resourceVersion`, `resource_characteristic`, `placeholder`) VALUES
(2, '\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0', '111111', '2222222222222', '333333', '44444444444', 'vxzc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `amari_radios`
--
ALTER TABLE `amari_radios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UUID` (`UUID`),
  ADD UNIQUE KEY `name` (`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `amari_radios`
--
ALTER TABLE `amari_radios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
