-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 14, 2022 at 03:15 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pwm`
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
  `cust_id` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `tel_num` int(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

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
  `employee_id` varchar(200) NOT NULL,
  `customer_id` varchar(200) NOT NULL,
  `activity_id` varchar(200) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `payment_invoice`
--

DROP TABLE IF EXISTS `payment_invoice`;
CREATE TABLE IF NOT EXISTS `payment_invoice` (
  `invoice_id` varchar(200) NOT NULL,
  `employee_id` varchar(200) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `remarktype`
--

DROP TABLE IF EXISTS `remarktype`;
CREATE TABLE IF NOT EXISTS `remarktype` (
  `remark_id` varchar(200) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`remark_id`)
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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
