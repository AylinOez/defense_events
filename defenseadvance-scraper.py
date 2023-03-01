import requests
from bs4 import BeautifulSoup


# getting a response object = "url" - all information is here now

for page in range(1,3):
    url = 'https://www.defenseadvancement.com/events/page/' + str(page)
    response= requests.get(url)
    soup= BeautifulSoup(response.content, 'html.parser')
    event_names= [event.text for event in soup.find_all('span', {'product-card-heading'})]
    event_start_date= [day.text for day in soup.find_all('span', {'class': 'webinar-day'})]
    event_month = [month.text for month in soup.find_all('span', {'class': 'webinar-month'})]
    event_duration= [days.text for days in soup.find_all('span', {'class': 'event-date'})]
    event_links= [links.find('a')['href'] for links in soup.find_all('span', {'product-card-heading'})]
    event_location= [location.text for location in soup.find_all('span', {'class': 'event-country'})]

print(event_names)
print(event_start_date)
print(event_month)
print(event_duration)
print(event_links)
print(event_location)