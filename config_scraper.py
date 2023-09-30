import requests
from bs4 import BeautifulSoup
import re



def making_soup(url):
     """
     Creates soup, writes it to a file, and returns it.
     
     Args:
        url (str): The URL to parse.
     
     Parameters:
        url (str): The URL of the website to scrape.
          
     Returns:
        soup (BeautifulSoup): A BeautifulSoup object containing the HTML content of all the scraped pages.
        file (file): A file containing the HTML content of all the scraped pages.
    """
     response = requests.get(url)
     soup = BeautifulSoup(response.content, 'html.parser')
         
     return soup


    
def find_event_box(soup, tag_name, class_name):
    """
    Finds all event boxes that contain event information.
    
    Parameters:
        soup (BeautifulSoup): Given BeautifulSoup.
        tag_name (str): The name of the HTML tag of event box.
        class_name (str): The value of the class attribute of event box.
    
    Returns:
        event_box (list): List of BeautifulSoup objects containing html content of all event boxes.
    """
    event_box = soup.find_all(tag_name, {'class': class_name})
    return event_box


def event_info(event_box, name_tag, name_attribute, day_tag, day_attribute, month_tag, month_attribute, location_tag, location_attribute):
    """
    Extracts event information from the content of all event boxes.
    
    Parameters:
        event_box: HTML elements to extract event information from.
        name_tag (str): The name of the HTML tag containing the event name.
        name_attribute (str): The value of the class attribute of the tag containing the event name.
        day_tag (str): The name of the HTML tag containing the event day.
        day_attribute (str): The value of the class attribute of the tag containing the event day.
        month_tag (str): The name of the HTML tag containing the event month.
        month_attribute (str): The value of the class attribute of the tag containing the event month.
        location_tag (str): The name of the HTML tag containing the event location.
        location_attribute (str): The value of the class attribute of the tag containing the event location.
    
    Returns:
        events (list): A list of dictionaries, where each dictionary represents an event and contains the event name, day, month, location, and link.
    """
    events = []

    for box in event_box:
        event_data = {}
        event_data['event_name'] = box.find(name_tag, {'class': name_attribute}).text.strip()
        event_data['event_day'] = box.find(day_tag, {'class': day_attribute}).text.strip()
        event_data['event_month'] = box.find(month_tag, {'class': month_attribute}).text.strip()
        #event_data['event_duration'] = box.find('span', {'class': 'event-date'}).text.strip()
        event_data['event_location'] = box.find(location_tag, {'class': location_attribute}).text.strip()
        event_data['event_link'] = box.find('a')['href']

        events.append(event_data)
        print(events)
        
    
    return events
