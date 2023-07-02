import mysql.connector

config= {
    'host':'localhost',
    'user':'user',
    'password':'password',
    'database':'defense_events',
    'raise_on_warnings': True
}

connecting_db = mysql.connector.connect(**config)

cursor = connecting_db.cursor()
query = r"LOAD DATA INFILE 'C:/Users/defense_events/defenseadvance.csv' INTO TABLE events FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS"
cursor.execute(query)

connecting_db.commit()

cursor.close()
connecting_db.close()

connecting_db.commit()




