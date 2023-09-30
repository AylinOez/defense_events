import unittest
import requests
from bs4 import BeautifulSoup
from scraper_config import *
from defenseadvance import *



for page in range(1,3):
    #send get request and parse
    url = f"https://www.defenseadvancement.com/events/page/{page}/"
    reponse= requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')
    
class TestDefenseAdvanceSoup(unittest.TestCase):
    def test_soup(self):
        self.assertEqual(control_defenseadvance == soup.prettify(), True)
        

    event_box = find_event_box(soup, 'span', {'class': 'product-box-details'})

    event = event_info(event_box, 'span', {'class': 'product-card-heading'}, 'span', {'class': 'webinar-day'},
                    'span', {'class': 'webinar-month'}, 'span', {'class': 'event-country'})

