USE defense_events;
DROP TABLE IF EXISTS events;
CREATE TABLE events (
  id int NOT NULL AUTO_INCREMENT,
  event_name varchar(50) NOT NULL,
  event_day int NOT NULL,
  event_month varchar(50) NOT NULL,
  event_location varchar(20) NOT NULL,
  event_link varchar(200) NOT NULL,
  UNIQUE KEY (id, event_name, event_day, event_month, event_location, event_link),
  PRIMARY KEY (id)
) 