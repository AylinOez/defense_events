import requests
from bs4 import BeautifulSoup


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
        
        event_data['event_name'] = event_box.find('span', {'class': 'product-box-heading'}).text.split()
        event_data['event_day'] = event_box.find('span', {'class': 'wenibar-day'}).text.split()
        event_data['event_month'] = event_box.find('span', {'class': 'webinar-month'}).text.split()
        event_data['event_duration'] = event_box.find('span', {'class': 'event_date'}).text.split()
        event_data['event_location'] = event_box.find('span', {'class': 'event_country'}).text.split()
        event_data['event_link'] = event_box.find('a')['href']
