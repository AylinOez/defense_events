import requests
from bs4 import BeautifulSoup
import mysql.connector


#create list to store events
events = []

#loop through pages
for page in range(1,3):
    #send get request and parse
    url = f"https://www.defenseadvancement.com/events/page/{page}/"
    reponse= requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    #get event boxes
    event_box = soup.find_all('span', {'class': 'product-box-details'})
    
    #lop through boxes and extract information
    for box in event_box:
        #create dict for each event
        event_data = {}
        
        event_data['event_name'] = box.find('span', {'product-card-heading'}).text.strip()
        event_data['event_day'] = box.find('span', {'class': 'webinar-day'}).text.strip()
        event_data['event_month'] = box.find('span', {'class': 'webinar-month'}).text.strip()
        event_data['event_duration'] = box.find('span', {'class': 'event-date'}).text.strip()
        event_data['event_location'] = box.find('span', {'class': 'event-country'}).text.strip()
        event_data['event_link'] = box.find('a')['href']

        events.append(event_data)

print(events)

config= {
    'host':'127.0.0.1',
    'user':'root',
    'password':'+7@t8tuP9?ejAJiS+LsP',
    'database':'defense_events',
    'raise_on_warnings': True
}
connecting_db = mysql.connector.connect(**config)

connecting_db.close()



