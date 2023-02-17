import requests
from bs4 import BeautifulSoup


# getting a response object = "url" - all information is here now
url= 'https://www.defenseadvancement.com/events/'
page= requests.get(url)

soup= BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

event_name = [event.text for event in soup.find_all('span', {'class': 'product-card-heading'})]


print(event_name)