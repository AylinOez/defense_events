from __future__ import print_function
import csv 

from config_scraper import * 
import requests
from bs4 import BeautifulSoup


url = 'https://www.defenseadvancement.com/events/'
#response = requests.get(url)
#soup = BeautifulSoup(response.content, 'html.parser')
#page_class = 'page-numbers'
page_tag= 'div'
page_attribute= 'pagination'
soup = making_soup(url, page_tag, page_attribute, max_pages=10)

event_box = find_event_box(soup, 'span', {'class': 'product-box-details'})
events = event_info(event_box, 'span', {'class': 'product-card-heading'}, 'span', {'class': 'webinar-day'},
                    'span', {'class': 'webinar-month'}, 'span', {'class': 'event-country'})
print(events)


with open('defenseadvance.csv', 'a', newline='') as csvfile:
    fieldnames= ['event_name', 'event_day', 'event_month', 'event_location', 'event_link']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in events:
        writer.writerow(row)