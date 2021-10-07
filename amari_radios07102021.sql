-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: rc_mysql_cont:3306
-- Generation Time: Oct 07, 2021 at 12:26 PM
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
  `resource_characteristic` varchar(2048) DEFAULT NULL,
  `placeholder` json DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `amari_radios`
--

INSERT INTO `amari_radios` (`id`, `UUID`, `name`, `description`, `resourceVersion`, `resource_characteristic`, `placeholder`) VALUES
(27, 'f24264fc-2763-11ec-bf26-a0a4c57c8193', 'AmarisoftClassic_dddd', 'Big Black Box', 'None', '{\'id\': \'f24264fc-2763-11ec-bf26-a0a4c57c8193\', \'href\': \'\', \'category\': \'gNodeB\', \'description\': \'Big Black Box\', \'end_operating_date\': None, \'name\': \'AmarisoftClassic_dddd\', \'resource_version\': None, \'start_operating_date\': None, \'activation_feature\': None, \'administrative_state\': None, \'attachment\': None, \'note\': None, \'operational_state\': None, \'place\': None, \'related_party\': None, \'resource_characteristic\': [{\'id\': \'f24264fd-2763-11ec-bf26-a0a4c57c8193\', \'name\': \'IP\', \'value_type\': \'string\', \'characteristic_relationship\': None, \'value\': {\'value\': \'1.2.3.4\'}, \'base_type\': None, \'schema_location\': None, \'type\': None}, {\'id\': \'f24264fe-2763-11ec-bf26-a0a4c57c8193\', \'name\': \'location\', \'value_type\': \'array\', \'characteristic_relationship\': None, \'value\': {\'value\': [123, 456]}, \'base_type\': None, \'schema_location\': None, \'type\': None}, {\'id\': \'f24264ff-2763-11ec-bf26-a0a4c57c8193\', \'name\': \'action\', \'value_type\': \'string\', \'characteristic_relationship\': None, \'value\': {\'value\': \'start/stop\'}, \'base_type\': None, \'schema_location\': None, \'type\': None}, {\'id\': \'f2426500-2763-11ec-bf26-a0a4c57c8193\', \'name\': \'action_parameters\', \'value_type\': \'object\', \'characteristic_relationship\': None, \'value\': {\'value\': {\'param1\': \'value1\', \'param2\': \'value2\'}}, \'base_type\': None, \'schema_location\': None, \'type\': None}], \'resource_relationship\': None, \'resource_specification\': None, \'resource_status\': None, \'usage_state\': None, \'base_type\': None, \'schema_location\': None, \'type\': None}', NULL),
(31, '422df46a-2767-11ec-bf26-a0a4c57c8193', 'AmarisoftClassic_2', 'Big Black Box', 'None', '{\'id\': \'422df46a-2767-11ec-bf26-a0a4c57c8193\', \'href\': \'\', \'category\': \'gNodeB\', \'description\': \'Big Black Box\', \'end_operating_date\': None, \'name\': \'AmarisoftClassic_2\', \'resource_version\': None, \'start_operating_date\': None, \'activation_feature\': None, \'administrative_state\': None, \'attachment\': None, \'note\': None, \'operational_state\': None, \'place\': None, \'related_party\': None, \'resource_characteristic\': [{\'id\': \'422df46b-2767-11ec-bf26-a0a4c57c8193\', \'name\': \'IP\', \'value_type\': \'string\', \'characteristic_relationship\': None, \'value\': {\'value\': \'11.22.33.44\'}, \'base_type\': None, \'schema_location\': None, \'type\': None}, {\'id\': \'422df46c-2767-11ec-bf26-a0a4c57c8193\', \'name\': \'location\', \'value_type\': \'array\', \'characteristic_relationship\': None, \'value\': {\'value\': [123, 456]}, \'base_type\': None, \'schema_location\': None, \'type\': None}, {\'id\': \'422df46d-2767-11ec-bf26-a0a4c57c8193\', \'name\': \'action\', \'value_type\': \'string\', \'characteristic_relationship\': None, \'value\': {\'value\': \'start/stop\'}, \'base_type\': None, \'schema_location\': None, \'type\': None}, {\'id\': \'422df46e-2767-11ec-bf26-a0a4c57c8193\', \'name\': \'action_parameters\', \'value_type\': \'object\', \'characteristic_relationship\': None, \'value\': {\'value\': {\'param1\': \'value1\', \'param2\': \'value2\'}}, \'base_type\': None, \'schema_location\': None, \'type\': None}], \'resource_relationship\': None, \'resource_specification\': None, \'resource_status\': None, \'usage_state\': None, \'base_type\': None, \'schema_location\': None, \'type\': None}', NULL);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
