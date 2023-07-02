import requests
from bs4 import BeautifulSoup

def making_soup(url, page_tag, page_attribute, max_pages=10):
    """
    Creates soup, then selects page numbers and the last element,
    check for multiple websites and then loops over them and
    creating a new Beautifulsoup object with data from all pages
    
    Parameters:
        url (str): The URL of the website to scrape.
        page_tag (str): The HTML tag of the page numbers.
        page_attribute (str): The attribute of the page tag.
        max_pages (int): The maximum number of pages to scrape. Default is 10.
    
    Returns:
        soup (BeautifulSoup): A BeautifulSoup object containing the HTML content of all the scraped pages.
    """
    response = requests.get(url)
    start_soup = BeautifulSoup(response.content, 'html.parser')
    page_links= start_soup.find(page_tag, class_ = page_attribute ).find_all('a')[-2].text
#+ '> a'
    if page_links:
        total_pages = int(page_links)
    else:
        total_pages = max_pages

    soup_list = []

    for page in range(1, total_pages+1):
        url_page= f'{url}/page/{page}/'
        response= requests.get(url_page, allow_redirects=False)
        soup_page= BeautifulSoup(response.content, 'html.parser')
        soup_list.append(soup_page)

    soup = BeautifulSoup('\n'.join([str(s) for s in soup_list]), 'html.parser')
    print(soup)
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


