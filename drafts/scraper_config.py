
def find_event_box(soup, tag_name, class_name):
     """
     Takes Beautifulsoup object, html tag and class name of event box
    and finds all event boxes that are available on the page

    Parameters:
    Beautifulsoup object
    HTML Tag name
    Class name

    Return 
    Event box locators
     """
     event_box = soup.find_all(tag_name, {'class': class_name})
     return event_box


def event_info(event_box, name_tag, name_attribute, day_tag, day_attribute, month_tag, month_attribute, location_tag, location_attribute):
      """
      Create empty list, get event information: Event name, -day, -month, -location, -link, create dictionary,
      stores data in seperate dictionaries and stores them in events list.

      Parameters:
      HTML tag and attributes
      Example: 'span', {'product-card-heading'}

      Returns:
      Event data dictionary
      """      
      events = []

      for box in event_box:
        #create dict for each event
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

