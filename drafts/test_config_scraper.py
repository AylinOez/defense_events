import pytest
from config_scraper import *

def test_making_soup():
    url = 'https://www.defenseadvancement.com/events/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    assert soup == making_soup(url)
    
    

