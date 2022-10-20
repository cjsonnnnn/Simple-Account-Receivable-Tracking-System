-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 20, 2022 at 08:12 AM
-- Server version: 5.7.36
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ethree`
--

-- --------------------------------------------------------

--
-- Table structure for table `activitytype`
--

DROP TABLE IF EXISTS `activitytype`;
CREATE TABLE IF NOT EXISTS `activitytype` (
  `activity_id` varchar(200) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `customer_id` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `tel_num` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `name`, `address`, `tel_num`, `password`, `status`) VALUES
('c-20221018180103', 'Jason', 'sersan an', '239123', 'sdkaks', 'not defined'),
('c-20221018180102', 'Jason', 'sersan an', '239123', 'sdkaks', 'not defined');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `employee_id` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `role_id` varchar(200) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `manager_activity`
--

DROP TABLE IF EXISTS `manager_activity`;
CREATE TABLE IF NOT EXISTS `manager_activity` (
  `manager_activity_id` varchar(200) NOT NULL,
  `employee_id` varchar(200) NOT NULL,
  `customer_id` varchar(200) NOT NULL,
  `activity_id` varchar(200) NOT NULL,
  PRIMARY KEY (`manager_activity_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `payment_invoice`
--

DROP TABLE IF EXISTS `payment_invoice`;
CREATE TABLE IF NOT EXISTS `payment_invoice` (
  `payment_invoice_id` varchar(200) NOT NULL,
  `invoice_id` varchar(200) NOT NULL,
  `employee_id` varchar(200) NOT NULL,
  PRIMARY KEY (`payment_invoice_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `roletype`
--

DROP TABLE IF EXISTS `roletype`;
CREATE TABLE IF NOT EXISTS `roletype` (
  `role_id` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sale_invoice`
--

DROP TABLE IF EXISTS `sale_invoice`;
CREATE TABLE IF NOT EXISTS `sale_invoice` (
  `invoice_id` varchar(200) NOT NULL,
  `sale_date` date NOT NULL,
  `payment_date` date NOT NULL,
  `total` int(200) NOT NULL,
  `employee_id` varchar(200) NOT NULL,
  `customer_id` varchar(200) NOT NULL,
  `remark_id` varchar(200) NOT NULL,
  PRIMARY KEY (`invoice_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sale_invoice`
--

INSERT INTO `sale_invoice` (`invoice_id`, `sale_date`, `payment_date`, `total`, `employee_id`, `customer_id`, `remark_id`) VALUES
('inv-20221018180738', '2022-10-18', '2022-11-17', 2100000, 'NDAK ADA', 'c-20221018180102', 'WAITING'),
('inv-20221018180740', '2022-10-18', '2022-11-17', 2100000, 'NDAK ADA', 'c-20221018180102', 'ACCEPTED'),
('inv-20221020104555', '2022-10-20', '2022-11-19', 2100000, 'NDAK ADA', 'c-20221018180102', 'ACCEPTED'),
('inv-20221020143514', '2022-10-20', '2023-01-18', 2100000, 'NDAK ADA', 'c-20221018180102', 'ACCEPTED'),
('inv-20221020143515', '2022-10-20', '2023-01-18', 2100000, 'NDAK ADA', 'c-20221018180102', 'ACCEPTED'),
('inv-20221020143600', '2022-10-20', '2023-01-18', 2100000, 'NDAK ADA', 'c-20221018180102', 'ACCEPTED'),
('inv-20221020143619', '2022-10-20', '2023-04-18', 492000, 'NDAK ADA', 'c-20221018180102', 'WAITING'),
('inv-20221020143636', '2022-10-20', '2023-04-18', 861000, 'NDAK ADA', 'c-20221018180102', 'WAITING'),
('inv-20221020145202', '2022-10-20', '2023-10-15', 1143000, 'NDAK ADA', 'c-20221018180102', 'WAITING');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
