import pytest
from config_scraper import *

def test_making_soup():
    """
    Tests the functionality of making_soup function.
    
    Parameters: None
    
    Returns: None
    
    Raises: AssertionError if the soup object is not created.
    """
    url = 'https://www.defenseadvancement.com/events/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    assert soup == making_soup(url)
    
    
def test_find_event_box():
    """
    Tests the functionality of find_event_box function.
    
    Parameters: None
    
    Returns: None
    
    Raises: AssertionError if the event_box is not found.
    """
    soup = making_soup('https://www.defenseadvancement.com/events/')
    tag_name = 'span'
    class_name = 'product-box-details'
    event_box = soup.find_all(tag_name, {'class': class_name})
    assert event_box == find_event_box(soup, tag_name, class_name)

def test_event_info():
    """
    Tests the functionality of event_info function.
    
    Parameters: None
    
    Returns: None
    
    Raises: AssertionError if the event information is not extracted.
    """
    soup = making_soup('https://www.defenseadvancement.com/events/')
    tag_name = day_tag = month_tag = location_tag = name_tag = 'span'
    class_name = 'product-box-details'
    
    name_attribute = 'product-card-heading'
    day_attribute = 'webinar-day'
    month_attribute = 'webinar-month'
    location_attribute = 'event-country'
    
    event_box = find_event_box(soup, tag_name, class_name)
    events = event_info(event_box, name_tag, name_attribute, day_tag, day_attribute,
                        month_tag, month_attribute, location_tag, location_attribute)
    
    assert events == event_info(event_box, name_tag, name_attribute, day_tag, day_attribute,
                        month_tag, month_attribute, location_tag, location_attribute)