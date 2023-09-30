from __future__ import print_function
import csv 

from config_scraper import * 
import requests
from bs4 import BeautifulSoup


url = 'https://www.defenseadvancement.com/events/'
#response = requests.get(url)
#soup = BeautifulSoup(response.content, 'html.parser')
#page_class = 'page-numbers'

soup = making_soup(url)
control_defenseadvance = soup.prettify()


tag_name = day_tag = month_tag = location_tag = name_tag = 'span'
class_name = 'product-box-details'

name_attribute = 'product-card-heading'
day_attribute = 'webinar-day'
month_attribute = 'webinar-month'
location_attribute = 'event-country'

event_box = find_event_box(soup, tag_name, class_name)
print(event_box)

events = event_info(event_box, name_tag, name_attribute, day_tag, day_attribute,
                    month_tag, month_attribute, location_tag, location_attribute)
print(events)


with open('defenseadvance.csv', 'a', newline='') as csvfile:
    fieldnames= ['event_name', 'event_day', 'event_month', 'event_location', 'event_link']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in events:
        writer.writerow(row)
        
