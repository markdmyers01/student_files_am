"""
    task6_1_standard_starter.py  -   Using JSON, Requests, and HTML Parsing (Soup)

    This task asks you to retrieve the JSON data at the following URL:

                https://eonet.gsfc.nasa.gov/api/v3/events

    This URL provides information of events tracked by NASA.

    You should view this data in a browser to get a feel for what it contains.  Keep that browser tab open
    and then perform the following tasks:

    1) Retrieve the JSON data at the URL mentioned above.  Extract all the "events".
    2) Determine how many total events are currently being tracked by NASA (at this API).
    3) Obtain a list all the different possible categories (titles) that are tracked.
    4) Display the titles of all the fires ('Wildfires' category type)
    5) Retrieve the Inciweb HTML home page of the first wildfire being tracked (if it exists).
       This should be found under the sources[0] property of the event object.
    6) Retrieve the HTML page from the URL in step 5.  Return the fire's description (Incident Overview section).
       Do this by invoking soup's select() method, providing the given selector.

    Note: if no internet access is available, uncomment the import mocklab statement below and you may proceed
          with the task.

"""
import sys

from bs4 import BeautifulSoup
import requests

# import mocklab                          # uncomment this line if no internet access is available

# Setting all global variables here
base_url = 'https://eonet.gsfc.nasa.gov'
api_path = '/api/v3/events'
all_categories = set()     # use for step 3
fires = []                 # use for step 4
selector = '.incident-main-content p'

# Making request to API endpoint
event_dict = requests.get(f'{base_url}{api_path}').json()
print(f'{base_url}{api_path}')
events = event_dict.get('events', [])
# print(events[:5])

# Getting all categories
for event in events:
    categories = event.get('categories', [])
    for category in categories:
        category_title = category.get('title')
        all_categories.add(category_title)

        # Get only wildfires
        if category_title == 'Wildfires':
            fires.append(event)

print(f'\nSeveral categories found across all events: {list(all_categories)}')

print(f'NASA tracking {len(events)} total events.')
print('\nDisplaying fires tracked:')
# print(fires[0])
print([fire.get("title") for fire in fires][:5])

first_fire = fires[10]
name = first_fire.get("title")
print(f'\nFirst fire listed: {name}')
sources = first_fire.get('sources')

if not sources:
    print(f'No Inciweb URL found for {name}')
    sys.exit(42)

url = sources[0].get('url')

print(f'Retrieving page for fire at: {url}')
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

print(f'\nDescription for {name}:')
selector = '.incident-main-content p'
print(soup.select(selector)[0].text)



