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
    

