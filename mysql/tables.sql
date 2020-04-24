-- Data Source
-- https://github.com/homaily/Saudi-Arabia-Regions-Cities-and-Districts


CREATE TABLE `regions` (
  `region_id` int(11) unsigned NOT NULL,
  `capital_city_id` int(11) NOT NULL,
  `code` varchar(2) NOT NULL DEFAULT '',
  `name_ar` varchar(64) NOT NULL DEFAULT '',
  `name_en` varchar(64) NOT NULL DEFAULT '',
  `center` point NOT NULL,
  `boundaries` polygon NOT NULL,
  `population` int(11) DEFAULT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `regions_lite` (
  `region_id` int(11) unsigned NOT NULL,
  `capital_city_id` int(11) NOT NULL,
  `code` varchar(2) NOT NULL DEFAULT '',
  `name_ar` varchar(64) NOT NULL DEFAULT '',
  `name_en` varchar(64) NOT NULL DEFAULT '',
  `population` int(11) DEFAULT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `cities` (
  `city_id` int(11) unsigned NOT NULL,
  `region_id` int(11) NOT NULL,
  `name_ar` varchar(64) NOT NULL DEFAULT '',
  `name_en` varchar(64) NOT NULL DEFAULT '',
  `center` point NOT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `cities_lite` (
  `city_id` int(11) unsigned NOT NULL,
  `region_id` int(11) NOT NULL,
  `name_ar` varchar(64) NOT NULL DEFAULT '',
  `name_en` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `districts` (
  `district_id` varchar(12) NOT NULL,
  `city_id` int(11) NOT NULL,
  `region_id` int(11) NOT NULL,
  `name_ar` varchar(64) NOT NULL DEFAULT '',
  `name_en` varchar(64) NOT NULL DEFAULT '',
  `boundaries` polygon NOT NULL,
  PRIMARY KEY (`district_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `districts_lite` (
  `district_id` varchar(12) NOT NULL,
  `city_id` int(11) NOT NULL,
  `region_id` int(11) NOT NULL,
  `name_ar` varchar(64) NOT NULL DEFAULT '',
  `name_en` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`district_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
