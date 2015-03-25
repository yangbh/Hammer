-- phpMyAdmin SQL Dump
-- version 4.2.9.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2015-03-25 11:01:08
-- 服务器版本： 5.6.19
-- PHP Version: 5.5.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hammer`
--

-- CREATE DATABASE IF NOT EXISTS Hammer DEFAULT CHARACTER SET utf8;
-- USE Hammer;

-- --------------------------------------------------------

--
-- 表的结构 `Dispatcher`
--

CREATE TABLE IF NOT EXISTS `Dispatcher` (
`ID` int(11) NOT NULL,
  `MAC` varchar(18) NOT NULL,
  `OS` varchar(32) NOT NULL,
  `IP` varchar(16) DEFAULT NULL,
  `Last_Time` int(11) DEFAULT NULL,
  `User_ID` int(11) NOT NULL,
  `Status` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `Plugin`
--

CREATE TABLE IF NOT EXISTS `Plugin` (
`ID` int(11) NOT NULL,
  `Name` varchar(128) NOT NULL,
  `Type` varchar(64) NOT NULL,
  `Author` varchar(32) NOT NULL,
  `Time` varchar(11) DEFAULT NULL,
  `Version` varchar(8) DEFAULT NULL,
  `Web` varchar(128) DEFAULT NULL,
  `Description` varchar(512) DEFAULT NULL,
  `Code` varchar(20480) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `Proxy`
--

CREATE TABLE IF NOT EXISTS `Proxy` (
`ID` int(11) NOT NULL,
  `IP_Addr` varchar(16) NOT NULL,
  `Port` int(11) NOT NULL,
  `Type` varchar(6) NOT NULL,
  `Address` varchar(1024) NOT NULL,
  `Latency` int(11) NOT NULL,
  `Reliability` int(8) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `Scan`
--

CREATE TABLE IF NOT EXISTS `Scan` (
`ID` int(11) NOT NULL,
  `Url` varchar(128) NOT NULL,
  `Start_Time` int(11) DEFAULT NULL,
  `End_Time` int(11) DEFAULT NULL,
  `Arguments` varchar(1024) NOT NULL,
  `Level` int(11) DEFAULT '0',
  `User_ID` int(11) NOT NULL,
  `Parent_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=563 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `Task`
--

CREATE TABLE IF NOT EXISTS `Task` (
`ID` int(11) NOT NULL,
  `Target` varchar(128) NOT NULL,
  `Start_Time` int(11) DEFAULT NULL,
  `End_Time` int(11) DEFAULT NULL,
  `Arguments` varchar(1024) NOT NULL,
  `User_ID` int(11) NOT NULL,
  `Dispatcher_ID` int(11) DEFAULT NULL,
  `Status` varchar(16) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `User`
--

CREATE TABLE IF NOT EXISTS `User` (
`ID` int(11) NOT NULL,
  `Name` varchar(32) NOT NULL,
  `Password` varchar(32) NOT NULL,
  `Is_Admin` tinyint(1) DEFAULT '0',
  `Token` varchar(64) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `Vuln`
--

CREATE TABLE IF NOT EXISTS `Vuln` (
`ID` int(11) NOT NULL,
  `Scan_ID` int(11) DEFAULT NULL,
  `Plugin_ID` int(11) DEFAULT NULL,
  `Vuln_Info` varchar(2048) DEFAULT NULL,
  `Level` int(11) DEFAULT '0',
  `IP_URL` varchar(256) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=10666 DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Dispatcher`
--
ALTER TABLE `Dispatcher`
 ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Plugin`
--
ALTER TABLE `Plugin`
 ADD PRIMARY KEY (`ID`), ADD UNIQUE KEY `UnName` (`Name`);

--
-- Indexes for table `Proxy`
--
ALTER TABLE `Proxy`
 ADD PRIMARY KEY (`ID`), ADD UNIQUE KEY `UnURL` (`IP_Addr`,`Port`,`Type`), ADD UNIQUE KEY `IP_Addr` (`IP_Addr`,`Port`,`Type`);

--
-- Indexes for table `Scan`
--
ALTER TABLE `Scan`
 ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Task`
--
ALTER TABLE `Task`
 ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
 ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Vuln`
--
ALTER TABLE `Vuln`
 ADD PRIMARY KEY (`ID`), ADD KEY `Plugin_ID` (`Plugin_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Dispatcher`
--
ALTER TABLE `Dispatcher`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Plugin`
--
ALTER TABLE `Plugin`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Proxy`
--
ALTER TABLE `Proxy`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Scan`
--
ALTER TABLE `Scan`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Task`
--
ALTER TABLE `Task`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `User`
--
ALTER TABLE `User`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `Vuln`
--
ALTER TABLE `Vuln`
MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- 限制导出的表
--

--
-- 限制表 `Vuln`
--
ALTER TABLE `Vuln`
ADD CONSTRAINT `vuln_ibfk_1` FOREIGN KEY (`Plugin_ID`) REFERENCES `Plugin` (`ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

--
-- 初始化`admin`
--
INSERT INTO User(Name,Password,Is_Admin) VALUES('admin','7e50507f61f9f3a6d1ce4249819f97ef','1');
