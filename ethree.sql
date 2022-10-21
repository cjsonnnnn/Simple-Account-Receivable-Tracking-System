-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 21, 2022 at 04:28 AM
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
('c-20221021045603', 'Kambing', 'begadang saia :)', '991', 'help!!!', 'BLACKLIST'),
('c-20221020170748', 'jason9', 'sersan aning', '16431', 'ja009', 'ACTIVE'),
('c-20221021034707', 'caleb09', 'sersan jaya', '0895239192', 'ca09', 'ACTIVE'),
('c-20221018180102', 'Jason', 'sersan aning jaya', '239123', 'sdkaks', 'ACTIVE');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `employee_id` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `role` varchar(200) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `name`, `password`, `role`) VALUES
('s-20221021041843', 'caleb', 'cal009', 'admin_sale'),
('m-20221021040617', 'Jason', 'jas009', 'manager'),
('f-20221021050038', 'Aku siapa?', 'ndaktau', 'admin_finance');

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
('inv-20221018180738', '2022-10-18', '2022-11-17', 2100000, 's-20221021041843', 'c-20221018180102', 'DECLINED'),
('inv-20221021053620', '2022-10-21', '2023-04-19', 492000, 's-20221021041843', 'c-20221020170748', 'ACCEPTED'),
('inv-20221020143619', '2022-10-20', '2023-04-18', 492000, 's-20221021041843', 'c-20221018180102', 'DECLINED'),
('inv-20221020143636', '2022-10-20', '2023-04-18', 861000, 'f-20221021050038', 'c-20221018180102', 'ACCEPTED'),
('inv-20221020145202', '2022-10-20', '2023-10-15', 1143000, 's-20221021041843', 'c-20221018180102', 'ACCEPTED'),
('inv-20221020151638', '2022-10-20', '2023-10-15', 508000, 's-20221021041843', 'c-20221018180102', 'DECLINED'),
('inv-20221020170927', '2022-10-20', '2023-10-15', 635000, 's-20221021041843', 'c-20221020170748', 'DECLINED'),
('inv-20221020185523', '2022-10-20', '2023-04-18', 123000, 's-20221021041843', 'c-20221020170748', 'DECLINED'),
('inv-20221020185635', '2022-10-20', '2023-10-15', 1143000, 's-20221021041843', 'c-20221020170748', 'DECLINED'),
('inv-20221021045800', '2022-10-21', '2023-04-19', 861000, 's-20221021041843', 'c-20221018180102', 'DECLINED');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
