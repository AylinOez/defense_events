from __future__ import print_function

import requests
from bs4 import BeautifulSoup

import mysql.connector
from datetime import date, datetime, timedelta

import csv 


for page in range(1,3):
    url = f"https://www.defenseadvancement.com/events/page/{page}/"
    reponse= requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    event_box = soup.find_all('span', {'class': 'product-box-details'})
    events=[]
    for box in event_box:
        event_data = {}
        event_data['event_name'] = box.find('span', {'product-card-heading'}).text.strip()
        event_data['event_day'] = box.find('span', {'class': 'webinar-day'}).text.strip()
        event_data['event_month'] = box.find('span', {'class': 'webinar-month'}).text.strip()
        #event_data['event_duration'] = box.find('span', {'class': 'event-date'}).text.strip()
        event_data['event_location'] = box.find('span', {'class': 'event-country'}).text.strip()
        event_data['event_link'] = box.find('a')['href']

        events.append(event_data)

print(events)


with open('defenseadvance.csv', 'a', newline='') as csvfile:
    fieldnames= ['event_name', 'event_day', 'event_month', 'event_location', 'event_link']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in events:
        writer.writerow(row)

config= {
    'host':'127.0.0.1',
    'user':'root',
    'password':'+7@t8tuP9?ejAJiS+LsP',
    'database':'defense_events',
    'raise_on_warnings': True
}

connecting_db = mysql.connector.connect(**config)

cursor = connecting_db.cursor()
query = r"LOAD DATA INFILE 'C:/Users/Lugina/Documents/GitHub/defense_events/defenseadvance.csv' INTO TABLE events FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS"
cursor.execute(query)

connecting_db.commit()

cursor.close()
connecting_db.close()

connecting_db.commit()




