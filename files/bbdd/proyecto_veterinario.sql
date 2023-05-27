-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-05-2023 a las 12:18:25
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_veterinario`
--
CREATE DATABASE IF NOT EXISTS `proyecto_veterinario` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `proyecto_veterinario`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vet_citas`
--

DROP TABLE IF EXISTS `vet_citas`;
CREATE TABLE IF NOT EXISTS `vet_citas` (
  `COD_CITA` varchar(255) NOT NULL,
  `FECHA_CITA` varchar(255) NOT NULL,
  `HORA` varchar(255) NOT NULL,
  `ESTABLECIMIENTO` varchar(255) NOT NULL,
  `DNI` varchar(9) NOT NULL,
  PRIMARY KEY (`COD_CITA`),
  KEY `DNI` (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vet_citas`
--

INSERT INTO `vet_citas` (`COD_CITA`, `FECHA_CITA`, `HORA`, `ESTABLECIMIENTO`, `DNI`) VALUES
('0419SOR', '04/07/2024', '19:00', 'SORIA', '25783302M'),
('1612MAD', '16/05/2023', '12:00', 'MADRID', '04566732O'),
('1819GUA', '18/05/2023', '19:00', 'GUADALAJARA', '04443285J'),
('2410GUA', '24/06/2023', '10:00', 'GUADALAJARA', '04443285J'),
('3114SEG', '31/07/2024', '14:00', 'SEGOVIA', '25783302M'),
('3118SEG', '31/05/2023', '18:00', 'SEGOVIA', '13354320K');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vet_clientes`
--

DROP TABLE IF EXISTS `vet_clientes`;
CREATE TABLE IF NOT EXISTS `vet_clientes` (
  `DNI` varchar(9) NOT NULL,
  `NOMBRE` varchar(255) NOT NULL,
  `APELLIDOS` varchar(255) NOT NULL,
  `TELEFONO` int(9) NOT NULL,
  PRIMARY KEY (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vet_clientes`
--

INSERT INTO `vet_clientes` (`DNI`, `NOMBRE`, `APELLIDOS`, `TELEFONO`) VALUES
('02555674S', 'JOSÉ', 'FRANCO', 676431207),
('04443285J', 'ANSELMO', 'GUEVARA', 657444329),
('04566732O', 'AINARA', 'LLOPIS', 678403211),
('13354320K', 'SARA', 'FUENTES', 604593326),
('14833294N', 'RUFINA', 'CAMPOY', 659304442),
('23666739X', 'RUBÉN', 'LOPES', 697345210),
('25783302M', 'MÁXIMO', 'GODOY', 640233194),
('34021775P', 'MARCOS', 'MARTÍ', 634220193);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vet_mascotas`
--

DROP TABLE IF EXISTS `vet_mascotas`;
CREATE TABLE IF NOT EXISTS `vet_mascotas` (
  `ID_MASCOTA` varchar(255) NOT NULL,
  `ANIMAL` varchar(255) NOT NULL,
  `RAZA` varchar(255) NOT NULL,
  `DANIO` varchar(255) NOT NULL,
  `DUENIO` varchar(255) NOT NULL,
  PRIMARY KEY (`ID_MASCOTA`),
  KEY `DUENIO` (`DUENIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vet_mascotas`
--

INSERT INTO `vet_mascotas` (`ID_MASCOTA`, `ANIMAL`, `RAZA`, `DANIO`, `DUENIO`) VALUES
('COAN02555674S', 'CONEJO', 'ANGORA INGLÉS', 'LEVE', '02555674S'),
('COAR13354320K', 'CONEJO', 'ARLEQUIN', 'LEVE', '13354320K'),
('GAPE14833294N', 'GATO', 'PERSA', 'LEVE', '14833294N'),
('PEBE04566732O', 'PERRO', 'BEAGLE', 'MODERADO', '04566732O'),
('ZORO14833294N', 'ZORRO', 'ROJO', 'GRAVE', '14833294N');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `vet_citas`
--
ALTER TABLE `vet_citas`
  ADD CONSTRAINT `vet_citas_ibfk_1` FOREIGN KEY (`DNI`) REFERENCES `vet_clientes` (`DNI`) ON DELETE CASCADE;

--
-- Filtros para la tabla `vet_mascotas`
--
ALTER TABLE `vet_mascotas`
  ADD CONSTRAINT `vet_mascotas_ibfk_1` FOREIGN KEY (`DUENIO`) REFERENCES `vet_clientes` (`DNI`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
