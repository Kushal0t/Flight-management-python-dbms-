-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: flight_management
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `flight_list`
--

DROP TABLE IF EXISTS `flight_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_list` (
  `flight_ID` varchar(10) NOT NULL,
  `departure_time` time DEFAULT NULL,
  `origin` varchar(20) DEFAULT NULL,
  `destination` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`flight_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_list`
--

LOCK TABLES `flight_list` WRITE;
/*!40000 ALTER TABLE `flight_list` DISABLE KEYS */;
INSERT INTO `flight_list` VALUES ('AI223','09:15:00','Delhi','Mumbai'),('SG101','12:34:00','Bengaluru','Kolkata'),('UK442','23:40:00','Chennai','Hyderabad');
/*!40000 ALTER TABLE `flight_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seatsai223`
--

DROP TABLE IF EXISTS `seatsai223`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seatsai223` (
  `seat_no` varchar(4) NOT NULL,
  `flight_ID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`seat_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seatsai223`
--

LOCK TABLES `seatsai223` WRITE;
/*!40000 ALTER TABLE `seatsai223` DISABLE KEYS */;
INSERT INTO `seatsai223` VALUES ('A1','AI223'),('A3','AI223'),('A5','AI223'),('A6','AI223'),('B1','AI223'),('B2','AI223'),('B4','AI223'),('B5','AI223'),('B6','AI223'),('B8','AI223'),('C1','AI223'),('C2','AI223'),('C4','AI223'),('C7','AI223'),('D3','AI223'),('D5','AI223'),('D6','AI223'),('D7','AI223'),('E1','AI223'),('E2','AI223'),('E4','AI223'),('E6','AI223'),('E7','AI223'),('F1','AI223'),('F3','AI223'),('F4','AI223'),('F5','AI223'),('F6','AI223'),('F7','AI223'),('F8','AI223');
/*!40000 ALTER TABLE `seatsai223` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seatssg101`
--

DROP TABLE IF EXISTS `seatssg101`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seatssg101` (
  `seat_no` varchar(2) NOT NULL,
  `flight_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`seat_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seatssg101`
--

LOCK TABLES `seatssg101` WRITE;
/*!40000 ALTER TABLE `seatssg101` DISABLE KEYS */;
INSERT INTO `seatssg101` VALUES ('A1','SG101'),('A3','SG101'),('A5','SG101'),('A8','SG101'),('B2','SG101'),('B4','SG101'),('B7','SG101'),('C1','SG101'),('C3','SG101'),('C4','SG101'),('C7','SG101'),('D2','SG101'),('D3','SG101'),('D5','SG101'),('D8','SG101'),('E1','SG101'),('E3','SG101'),('E4','SG101'),('E6','SG101'),('E8','SG101'),('F2','SG101'),('F3','SG101'),('F4','SG101'),('F6','SG101'),('F7','SG101'),('F8','SG101');
/*!40000 ALTER TABLE `seatssg101` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seatsuk442`
--

DROP TABLE IF EXISTS `seatsuk442`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seatsuk442` (
  `seat_no` varchar(5) NOT NULL,
  `flight_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`seat_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seatsuk442`
--

LOCK TABLES `seatsuk442` WRITE;
/*!40000 ALTER TABLE `seatsuk442` DISABLE KEYS */;
INSERT INTO `seatsuk442` VALUES ('A2','UK442'),('A3','UK442'),('A6','UK442'),('B1','UK442'),('B3','UK442'),('B5','UK442'),('B8','UK442'),('C2','UK442'),('C4','UK442'),('C6','UK442'),('C8','UK442'),('D1','UK442'),('D4','UK442'),('D6','UK442'),('D7','UK442'),('E2','UK442'),('E5','UK442'),('E7','UK442'),('F1','UK442'),('F2','UK442'),('F4','UK442'),('F5','UK442'),('F7','UK442'),('F8','UK442');
/*!40000 ALTER TABLE `seatsuk442` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `booking_ID` varchar(20) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `seat` varchar(4) DEFAULT NULL,
  `flight_ID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`booking_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-09 12:08:47
