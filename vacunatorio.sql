-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.5.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Volcando datos para la tabla vacunatorio.paciente: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` (`rutpaciente`, `nombrepaciente`, `fechanacimiento`) VALUES
	('12333444-5', 'Kevin Espacio', '1996-04-27'),
	('13333333-3', 'killua zoldyck', '2018-11-18'),
	('14444444-4', 'Jesus de Nazareth', '2020-02-05'),
	('15666666-7', 'Francisco Villa', '1998-09-01'),
	('17666555-4', 'Camilo Septimo', '1900-01-15'),
	('19222222-5', 'Marco Jimenez', '1900-05-20'),
	('19666111-4', 'Michelle piñera', '2018-01-01'),
	('19888777-6', 'Juano Medino', '1980-03-12'),
	('55555555-5', 'Juana Medina', '2015-07-01');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;

-- Volcando datos para la tabla vacunatorio.vacuna: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `vacuna` DISABLE KEYS */;
INSERT INTO `vacuna` (`nombreenfermedad`, `fechallegada`) VALUES
	('covid-19', '2020-03-20'),
	('HPV', '2019-03-05'),
	('Meningococo', '2019-04-01'),
	('MMR', '2020-04-01'),
	('sarna', '2019-05-07');
/*!40000 ALTER TABLE `vacuna` ENABLE KEYS */;

-- Volcando datos para la tabla vacunatorio.vacunados: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `vacunados` DISABLE KEYS */;
INSERT INTO `vacunados` (`nombreenfermedad`, `rutpaciente`, `fechavacuna`) VALUES
	('covid-19', '13333333-3', '2020-04-02'),
	('covid-19', '19222222-5', '2020-03-27'),
	('HPV', '14444444-4', '2020-03-21'),
	('Meningococo', '55555555-5', '2020-04-02'),
	('MMR', '12333444-5', '2020-04-02'),
	('MMR', '14444444-4', '2020-04-02'),
	('MMR', '19666111-4', '2020-04-02'),
	('MMR', '55555555-5', '2020-04-02');
/*!40000 ALTER TABLE `vacunados` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
