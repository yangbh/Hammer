-- phpMyAdmin SQL Dump
-- version 4.2.9.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2015-06-22 12:53:18
-- 服务器版本： 5.6.19
-- PHP Version: 5.5.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Hammer`
--

-- --------------------------------------------------------

--
-- 表的结构 `Config`
--

CREATE TABLE IF NOT EXISTS `Config` (
  `ID` int(11) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `User_ID` int(11) NOT NULL,
  `Config` text NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `AutoI` varchar(16) NOT NULL DEFAULT '1|1|1|1|1|0|0',
  `Description` varchar(2048) DEFAULT NULL,
  `IsDefault` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Config`
--

INSERT INTO `Config` (`ID`, `Name`, `User_ID`, `Config`, `Time`, `AutoI`, `Description`, `IsDefault`) VALUES
(1, 'basic', 1, '{"Sensitive_Info":{"backupfile":{"timeout":3000},"compressedfile":{"timeout":3000},"probefile":{"timeout":3000},"robots":[],"senpath":{"timeout":3000}},"Info_Collect":{"subdomain":{"auto_add":true,"timeout":60},"crawler":{"same_host":true,"cookies":"","timeout":3000,"keyword":"","max_count":500,"headers":"","same_domain":true,"time":21600,"ssl_verify":false,"max_depth":5},"portscan":{"auto_add":true,"ports":"21,22,23,25,110,53,67,80,1521,1526,3306,3389,4899,8580,873,443,465,993,995,2082,2083,2222,2601,2604,3128,3312,3311,4440,6082,6379,7001,7778,8000-9090,8080,8888,8083,8089,9200,10000,11211,11211,28017,27017","timeout":600,"argument":"-sV "},"neighborhost":{"auto_add":true,"timeout":20},"whatweb":{"timeout":300}},"System":{"dnszone":{"timeout":300},"elasticsearch_rce":{"ports":[9200]},"iismethod":[],"iisshort":[],"mongodb_unauth_access":{"ports":[27017]},"ms12020":{"ports":[3389]},"ms15034":[],"openssl":{"ports":[993,995]},"phpmoadmin_rce":[],"phpmoadmin_rce_2":[],"phpmyadmin_null_password":[],"rsync_unauth_access":{"ports":[873]},"struts2_remote_cmd_exec":[],"webdav":[],"elastisearch_groovy_rce_cve_2015_1427":{"ports":[9200]}},"Common":{"fileinclusion":{"timeout":600},"sqlinjection":{"timeout":600}},"Others":[],"Web_Applications":{"appcms_backup_files_download":[],"bo_blog_tag_php_xss":[],"CMS53KF_file_download":[],"Comsenz_uctools":[],"cscms_index_php_open_bang_sql_injection":[],"DeDecms5_7_plus_recommend_php_injection":[],"DeDecms5_7minggan_info":[],"dedecms_downloadphp_url_redict":[],"discuz7_2fap_php_sqlinject":[],"discuz_x2_5_path_disclosure":[],"Discuz_X3_uctools":[],"drupal7_31_sqlinject":[],"ecshop_2_6_2_7_GBK_sql_injection":[],"ecshop_flow_php_SQL_Injection":[],"ecshop_path_info":[],"ecshop_user_php_signin_action_sqli":[],"espcms_search_inject":[],"espcms_sql_inject":[],"IP_Board_3_4_7_sql_inject":[],"Kindeditor_mulu_bianli":[],"MetInfo_GETSHELL":[],"MvmMall_SQL_INJECTION":[],"mvmmall_unauthentication_remote_code_exec":[],"phpcms_preview_php_sql_injection":[],"phpmps_v9_authkey_print":[],"shopex_phpinfo_disclosure":[],"wordpress_392_formatting_xss":[],"WordPress_cp_multi_view_calendar1_1_4_SQL_Injection":[],"wordpress_reflect_xss":[],"WordPress_SEO_BY_Yoast_1_7_3_3_SQL_Injection":[],"wordpress_xmlrpc":[]},"Weak_Password":{"sshcrack":{"timeout":3000},"tomcatcrack":{"timeout":3000}}}', '2015-06-18 10:36:05', '1|1|1|1|1|1|0', '基础', 1),
(2, 'test', 1, '{"Info_Collect":{"subdomain":{"auto_add":true,"timeout":60},"crawler":{"same_host":true,"cookies":"","timeout":3000,"keyword":"","max_count":500,"headers":"","same_domain":true,"time":21600,"ssl_verify":false,"max_depth":5},"portscan":{"auto_add":true,"ports":"21,22,23,25,110,53,67,80,1521,1526,3306,3389,4899,8580,873,443,465,993,995,2082,2083,2222,2601,2604,3128,3312,3311,4440,6082,6379,7001,7778,8000-9090,8080,8888,8083,8089,9200,10000,11211,11211,28017,27017","timeout":600,"argument":"-sV "},"neighborhost":{"auto_add":true,"timeout":20},"whatweb":{"timeout":300}},"Common":{"fileinclusion":{"timeout":600},"sqlinjection":{"timeout":600}},"Sensitive_Info":{"backupfile":{"timeout":3000},"compressedfile":{"timeout":3000},"probefile":{"timeout":3000},"robots":[],"senpath":{"timeout":3000}},"System":{"dnszone":{"timeout":300},"elasticsearch_rce":{"ports":[9200]},"iismethod":[],"iisshort":[],"mongodb_unauth_access":{"ports":[27017]},"ms12020":{"ports":[3389]},"ms15034":[],"openssl":{"ports":[993,995]},"phpmoadmin_rce":[],"phpmoadmin_rce_2":[],"phpmyadmin_null_password":[],"rsync_unauth_access":{"ports":[873]},"struts2_remote_cmd_exec":[],"webdav":[],"elastisearch_groovy_rce_cve_2015_1427":{"ports":[9200]}},"Weak_Password":{"sshcrack":{"timeout":3000},"tomcatcrack":{"timeout":3000}},"Web_Applications":{"appcms_backup_files_download":[],"bo_blog_tag_php_xss":[],"CMS53KF_file_download":[],"Comsenz_uctools":[],"cscms_index_php_open_bang_sql_injection":[],"DeDecms5_7_plus_recommend_php_injection":[],"DeDecms5_7minggan_info":[],"dedecms_downloadphp_url_redict":[],"discuz7_2fap_php_sqlinject":[],"discuz_x2_5_path_disclosure":[],"Discuz_X3_uctools":[],"drupal7_31_sqlinject":[],"ecshop_2_6_2_7_GBK_sql_injection":[],"ecshop_flow_php_SQL_Injection":[],"ecshop_path_info":[],"ecshop_user_php_signin_action_sqli":[],"espcms_search_inject":[],"espcms_sql_inject":[],"IP_Board_3_4_7_sql_inject":[],"Kindeditor_mulu_bianli":[],"MetInfo_GETSHELL":[],"MvmMall_SQL_INJECTION":[],"mvmmall_unauthentication_remote_code_exec":[],"phpcms_preview_php_sql_injection":[],"phpmps_v9_authkey_print":[],"shopex_phpinfo_disclosure":[],"wordpress_392_formatting_xss":[],"WordPress_cp_multi_view_calendar1_1_4_SQL_Injection":[],"wordpress_reflect_xss":[],"WordPress_SEO_BY_Yoast_1_7_3_3_SQL_Injection":[],"wordpress_xmlrpc":[]}}', '2015-06-18 10:36:05', '1|1|1|1|1|1|1', '测试', 0);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Dispatcher`
--

INSERT INTO `Dispatcher` (`ID`, `MAC`, `OS`, `IP`, `Last_Time`, `User_ID`, `Status`) VALUES
(1, '3c:15:c2:c5:c8:96', 'Darwin', '127.0.0.1', 1432966678, 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `Plugin`
--

CREATE TABLE IF NOT EXISTS `Plugin` (
`ID` int(11) NOT NULL,
  `Name` varchar(128) NOT NULL,
  `File` varchar(256) NOT NULL,
  `Type` varchar(64) NOT NULL,
  `Author` varchar(32) NOT NULL,
  `Time` varchar(11) DEFAULT NULL,
  `Version` varchar(8) DEFAULT NULL,
  `Web` varchar(128) DEFAULT NULL,
  `Description` varchar(512) DEFAULT NULL,
  `Code` text NOT NULL,
  `Opts` varchar(1024) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Plugin`
--
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Scan`
--
-- --------------------------------------------------------

--
-- 表的结构 `Task`
--

CREATE TABLE IF NOT EXISTS `Task` (
`ID` int(11) NOT NULL,
  `Target` varchar(256) NOT NULL,
  `Start_Time` int(11) DEFAULT NULL,
  `End_Time` int(11) DEFAULT NULL,
  `Arguments` varchar(10240) NOT NULL,
  `User_ID` int(11) NOT NULL,
  `Dispatcher_ID` int(11) DEFAULT NULL,
  `Status` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Task`
--
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `User`
--

INSERT INTO `User` (`ID`, `Name`, `Password`, `Is_Admin`, `Token`) VALUES
(1, 'admin', '7e50507f61f9f3a6d1ce4249819f97ef', 1, 'jFXzKP2tlGZNgkPyhTmR1jLej6KzSIfC');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `Vuln`
--
--
-- Indexes for dumped tables
--

--
-- Indexes for table `Config`
--
ALTER TABLE `Config`
 ADD PRIMARY KEY (`ID`), ADD KEY `User_ID` (`User_ID`);

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
-- 限制表 `Config`
--
ALTER TABLE `Config`
ADD CONSTRAINT `config_ibfk_1` FOREIGN KEY (`User_ID`) REFERENCES `User` (`ID`);

--
-- 限制表 `Vuln`
--
ALTER TABLE `Vuln`
ADD CONSTRAINT `vuln_ibfk_1` FOREIGN KEY (`Plugin_ID`) REFERENCES `Plugin` (`ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
