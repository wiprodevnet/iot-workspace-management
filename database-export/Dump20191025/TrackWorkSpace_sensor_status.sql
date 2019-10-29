-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: TrackWorkSpace
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sensor_status`
--

DROP TABLE IF EXISTS `sensor_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor_status` (
  `sensor_status_idn` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_serial_no` varchar(45) NOT NULL,
  `sensor_status` varchar(45) NOT NULL,
  `sensor_idn` int(11) DEFAULT NULL,
  `crt_dt` datetime DEFAULT NULL,
  `upd_dt` datetime DEFAULT NULL,
  PRIMARY KEY (`sensor_status_idn`),
  UNIQUE KEY `sensor_serial_no_UNIQUE` (`sensor_serial_no`),
  KEY `fk_sensor_status_1_idx` (`sensor_idn`)
) ENGINE=InnoDB AUTO_INCREMENT=4188 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_status`
--

LOCK TABLES `sensor_status` WRITE;
/*!40000 ALTER TABLE `sensor_status` DISABLE KEYS */;
INSERT INTO `sensor_status` VALUES (4183,'PS100-10001','OFF',1,'2019-10-22 11:17:55','2019-10-24 18:35:15'),(4184,'PS100-10002','OFF',10,'2019-10-22 11:17:55','2019-10-24 18:35:15'),(4185,'PS100-10003','OFF',11,'2019-10-22 11:17:55','2019-10-24 18:35:15'),(4186,'PS100-10004','OFF',12,'2019-10-22 11:17:55','2019-10-24 18:35:15'),(4187,'PS100-10005','ON',13,'2019-10-22 11:17:55','2019-10-24 18:35:15');
/*!40000 ALTER TABLE `sensor_status` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-25 15:54:35
