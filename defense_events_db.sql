USE defense_events;
CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(50) DEFAULT NULL,
  `event_date` date DEFAULT NULL,
  `event_location` varchar(20) DEFAULT NULL,
  `event_link` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) 